setlocal enabledelayedexpansion

set "pattern= "
set "replace=_"

for %%I in (*.json) do (
    set "file=%%~I"
    ren "%%I" "!file:%pattern%=%replace%!"
)
