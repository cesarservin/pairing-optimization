import pandas as pd


def po(dataframe: pd.DataFrame, constraints: list, components: list, resource: list) -> pd.DataFrame:
    """Pairing Optimization (po) generates pairs (kits, bundles, or sets) of products based on constraints

    Args:
        dataframe (pd.DataFrame): dataframe with columns/features
        constraints (list): constraint or characteristics that every pair must have in common
        components (list): components that makes up the pair
        resource (list): resource numeric variable to pair

    Returns:
        pd.DataFrame: dataframe with maximum number of possible pairing that can be generated based on the requirements
    """
    import numpy as np
    import pandas as pd

    # group data based on the determined constraints and compenents that can be created with the resources
    all_fields = constraints + components

    df_determine_group = dataframe.groupby(all_fields)[resource].sum().reset_index()
    # shape dataframe to find pairing items/components for the given constraints
    df_group_pt = pd.pivot_table(df_determine_group, index=constraints, columns=components, fill_value=0)
    # determine if pair is possible
    df_group_pt["pairfilter"] = np.multiply(df_group_pt.iloc[:, 0].values, df_group_pt.iloc[:, 1].values)
    # find successful pairs
    df_group_pt_set = df_group_pt.loc[df_group_pt["pairfilter"] != 0].drop(columns=df_group_pt.columns[[2]], axis=1)
    # reshape dataframe back to initial shape where features are each column to find max number of pairs
    df_group_pt_set_stack = df_group_pt_set.stack(future_stack=True)
    # find max amoutn of pairs possible without orphans given the contraints and resource
    # Min resource assure there are no orphans
    df_group_min = df_group_pt_set_stack.groupby(constraints)[df_group_pt_set_stack.columns[0]].min().reset_index()

    return df_group_min


def max_streak(dataframe: pd.DataFrame, range_start: int, range_end: int) -> pd.DataFrame:
    """Calculate streaks of positive values in a DataFrame also
    referred to as a "streak counting algorithm" or simply a "streak counter.

    Args:
        dataframe (pd.DataFrame): wide format where the columnts to be counter \
            are columns and characteristics as the beginning
        range_start (int): start of values index
        range_end (int): end of values index

    Returns:
        pd.DataFrame: dataframe with a new column showing the longest continous streak
    """

    # find all products with a possible set
    # https://stackoverflow.com/questions/45964740/python-pandas-cumsum-with-reset-everytime-there-is-a-0
    # https://stackoverflow.com/questions/51278155/python-dataframe-counter-on-a-column
    # https://stackoverflow.com/questions/41420822/conditional-cumulative-sum-in-python-pandas
    # https://stackoverflow.com/questions/54737294/how-to-reset-cumulative-sum-every-time-there-is-a-nan-in-a-pandas-dataframe

    # This line checks if the values in the DataFrame are positive
    positive = dataframe.iloc[:, range_start:range_end] > 0

    # This line calculates the cumulative sum along the along columns
    # for the positive values, effectively creating a counter for streaks of positive values.
    counter = positive.cumsum(axis=1)

    # This line fills the NaN values in 'counter' with the last valid observation along columns,
    # effectively propagating the last valid value forward to fill the NaNs.
    trailing_counter = counter.where(~positive, axis=0).ffill(axis=1).fillna(0).astype(int)

    # This line calculates the difference between the cumulative sum 'counter' and the trailing counts after a restart,
    # which effectively gives the length of each streak of positive values.
    d = counter - trailing_counter

    # This line assigns the maximum streak length along columns to a new column 'NumOfContinous' in the DataFrame.
    dataframe["maxcontinous"] = d.max(axis=1)

    return dataframe
