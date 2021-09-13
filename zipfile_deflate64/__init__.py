# isort: skip_file

# Has the side effect of applying patches
try:
    from . import _zipfile  # noqa: F401
except (ImportError, SyntaxError):
    # allow anyway to allow zipfile39
    import zipfile
    zipfile.ZIP_DEFLATED64 = 9

# Re-export everything, so this can be used in place of zipfile
from zipfile import *  # noqa: F401, F403

# ZIP_DEFLATED64 is not a part of zipfile.__all__
from zipfile import ZIP_DEFLATED64  # type: ignore[attr-defined] # noqa: F401
