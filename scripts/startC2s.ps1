# Get the parent directory
$distDir = Split-Path -Parent (Get-Location)

# Create script blocks with proper variable passing
$scriptBlock1 = {
    param($distDir)
    try {
        $npmPath = Join-Path (Join-Path $distDir "lib") "openmct"
        Write-Host "Starting npm in $npmPath"
        npm start --prefix $npmPath
    } catch {
        Write-Error $_.Exception.Message
    }
}

$scriptBlock2 = {
    param($distDir)
    try {
        $mvnPath = Join-Path (Join-Path $distDir "lib") "yamcs"
        Write-Host "Starting mvn in $mvnPath"
        mvn yamcs:run --file $mvnPath
    } catch {
        Write-Error $_.Exception.Message
    }
}

# Start the jobs with proper parameter passing
$job1 = Start-Job -ScriptBlock $scriptBlock1 -ArgumentList $distDir
$job2 = Start-Job -ScriptBlock $scriptBlock2 -ArgumentList $distDir

# Register Ctrl+C handler properly
$null = [Console]::TreatControlCAsInput = $true

try {
    Write-Host "Jobs started. Press Ctrl+C to stop..."
    
    # Main loop to handle both job output and Ctrl+C
    while ($true) {
        # Check for Ctrl+C
        if ([Console]::KeyAvailable) {
            $key = [Console]::ReadKey($true)
            if ($key.Key -eq 'C' -and $key.Modifiers -eq 'Control') {
                throw "CtrlC"
            }
        }

        # Stream output from jobs
        Receive-Job -Job $job1 | ForEach-Object { Write-Host "[npm] $_" }
        Receive-Job -Job $job2 | ForEach-Object { Write-Host "[mvn] $_" }

        # Check if jobs are still running
        if (($job1.State -eq 'Completed' -or $job1.State -eq 'Failed') -and 
            ($job2.State -eq 'Completed' -or $job2.State -eq 'Failed')) {
            break
        }

        Start-Sleep -Milliseconds 100
    }
} catch {
    if ($_.Exception.Message -eq "CtrlC") {
        Write-Host "`nCtrl+C detected. Stopping jobs..."
    } else {
        Write-Host "An error occurred: $($_.Exception.Message)"
    }
} finally {
    # Stop and clean up jobs
    $job1, $job2 | ForEach-Object {
        if ($_ -ne $null) {
            Stop-Job -Job $_ -ErrorAction SilentlyContinue
            Remove-Job -Job $_ -Force -ErrorAction SilentlyContinue
        }
    }
    Write-Host "Jobs stopped and cleaned up."
}