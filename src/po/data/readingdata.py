def file_path_finder(file_name: str) -> str:
    """generates path from folder name called data and file name.

    Args:
        file_name (str): file name

    Returns:
        df_dir (str): directory of file
    """
    import glob
    import os

    main_dir = os.path.dirname(os.getcwd())
    rawdata_dir = os.path.join(main_dir, "data", file_name)
    df_dir = glob.glob(rawdata_dir)[0]
    return df_dir
