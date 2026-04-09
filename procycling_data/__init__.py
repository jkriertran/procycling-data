import pkg_resources

def get_data_path(filename):
    """
    Returns the absolute path to a data file within the procycling_data package.

    Args:
        filename (str): The relative path to the file within the
                        procycling_data/raw/procycling_proteam_analysis/ directory.
                        Example: 'wt_rosters_md/ag2r-citroen-team-2022.md'

    Returns:
        str: The absolute path to the data file.
    """
    return pkg_resources.resource_filename(
        __name__,
        f'data/raw/procycling_proteam_analysis/{filename}'
    )

def list_data_files(subdirectory=None):
    """
    Lists all data files within a specified subdirectory of the procycling_data package.

    Args:
        subdirectory (str, optional): The subdirectory to list files from.
                                      Example: 'wt_rosters_md'. If None, lists all files.

    Returns:
        list: A list of relative paths to the data files.
    """
    base_path = 'data/raw/procycling_proteam_analysis'
    if subdirectory:
        base_path = f'{base_path}/{subdirectory}'

    # This is a simplified example. In a real package, you might need to iterate
    # through directories or use a more robust method to list files if pkg_resources
    # does not directly support listing contents of a directory within a package.
    # For now, we assume direct access via known paths.
    # A more complete solution might involve iterating through the actual file system
    # after the package is installed, or maintaining a manifest.
    print(f"Warning: list_data_files is a placeholder and may not list all files correctly after installation.")
    return [] # Placeholder, as pkg_resources.resource_listdir is not always reliable for nested dirs

