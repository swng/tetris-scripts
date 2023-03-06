@echo off
rem Makes the cmd line not output each command as it's being used
set coverPath="C:\Users\swng\Source\solution-finder-1.42\output\cover.csv"
rem Set a variable to the path the cover file is in.
rem set /p coverPath="What should we set our cover path to? " Will allow you to set it to anything, set /p prompts the user.
xcopy %coverPath% ".\" /Y
rem cover.csv is assumed to be at coverPath, %~dp0 is the batch file's directory, /Y means overwrite if needed.
rem pause