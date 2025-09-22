param (
    [string]$ExecutablePath
)

# ファイルが存在するか確認
if ($ExecutablePath -ne "" -and !(Test-Path $ExecutablePath)) {
    Write-Error "The file at path $ExecutablePath does not exist."
    exit 1
}

# プロセスの開始
$process = Start-Process -FilePath $ExecutablePath -NoNewWindow -PassThru
$handle = $process.Handle # cache proc.Handle
Write-Output "Launched the executable."


# プロセスの終了を待つ
$process.WaitForExit()

# プロセスがエラーで終了した場合、エラーメッセージを表示
if ($process.ExitCode -ne 0) {
    Write-Error "The process ended with an error. Exit code was: $($process.ExitCode)"
    exit 1
}
$handle=0

Write-Output "Process completed successfully."
