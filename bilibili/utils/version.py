def get_version(version: tuple[int, int, int, str, int] = None):
    """Return a PEP 440-compliant version number from VERSION."""
    if version is None:
        from bilibili import VERSION as version
    version = get_complete_version(version)

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = [.devN] - for dev releases

    main = get_main_version(version)

    sub = ""
    if version[3] == "dev":
        sub = ".dev" + str(version[4])

    return main + sub


def get_main_version(version: tuple[int, int, int, str, int]):
    """Return main version (X.Y[.Z]) from VERSION."""
    version = get_complete_version(version)
    parts = 2 if version[2] == 0 else 3
    return ".".join(str(x) for x in version[:parts])


def get_complete_version(version: tuple[int, int, int, str, int]):
    """
    check for correctness of the tuple provided.
    """
    assert len(version) == 5
    assert version[3] in ("dev", "final")

    return version
