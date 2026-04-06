# VHS documentation
#
# Output:
#   Output <path>.gif               Create a GIF output at the given <path>
#   Output <path>.mp4               Create an MP4 output at the given <path>
#   Output <path>.webm              Create a WebM output at the given <path>
#
# Require:
#   Require <string>                Ensure a program is on the $PATH to proceed
#
# Settings:
#   Set FontSize <number>           Set the font size of the terminal
#   Set FontFamily <string>         Set the font family of the terminal
#   Set Height <number>             Set the height of the terminal
#   Set Width <number>              Set the width of the terminal
#   Set LetterSpacing <float>       Set the letter spacing of the terminal
#   Set LineHeight <float>          Set the line height of the terminal
#   Set LoopOffset <float>%         Set the starting frame offset for the GIF loop
#   Set Theme <json|string>         Set the theme of the terminal
#   Set Padding <number>            Set the padding of the terminal
#   Set Framerate <number>          Set the framerate of the recording
#   Set PlaybackSpeed <float>       Set the playback speed of the recording
#
# Sleep:
#   Sleep <time>                    Sleep for a set amount of <time> in seconds
#
# Type:
#   Type[@<time>] "<characters>"    Type <characters> into the terminal with a
#                                   <time> delay between each character
#
# Keys:
#   Backspace[@<time>] [number]     Press the Backspace key
#   Down[@<time>] [number]          Press the Down key
#   Enter[@<time>] [number]         Press the Enter key
#   Space[@<time>] [number]         Press the Space key
#   Tab[@<time>] [number]           Press the Tab key
#   Left[@<time>] [number]          Press the Left Arrow key
#   Right[@<time>] [number]         Press the Right Arrow key
#   Up[@<time>] [number]            Press the Up Arrow key
#   Down[@<time>] [number]          Press the Down Arrow key
#   Ctrl+<key>                      Press the Control key + <key> (e.g. Ctrl+C)
#
# Display:
#   Hide                            Hide the subsequent commands from the output
#   Show                            Show the subsequent commands in the output

Output demo.gif

Require task-tracker

Set FontSize 16
Set Width 1200
Set Height 700
Set Theme "Catppuccin Mocha"
Set Padding 20
Set LoopOffset 80%
Set PlaybackSpeed 1.0

Hide
Type "clear" Enter
Sleep 500ms
Show

# Title
Type "# Task Tracker Demo 📝" Sleep 500ms Enter
Sleep 1s

# Show help
Type "task-tracker --help" Sleep 500ms Enter
Sleep 3s

# Add some tasks
Type "task-tracker add 'Build awesome CLI application'" Sleep 500ms Enter
Sleep 1s

Type "task-tracker add 'Write comprehensive documentation'" Sleep 500ms Enter
Sleep 1s

Type "task-tracker add 'Create demo GIF with VHS'" Sleep 500ms Enter
Sleep 1.5s

# List all tasks
Type "task-tracker list" Sleep 500ms Enter
Sleep 2s

# Mark first task as in-progress
Type "task-tracker mark-in-progress 1" Sleep 500ms Enter
Sleep 1.5s

# Update a task
Type "task-tracker update 2 'Write comprehensive documentation with examples'" Sleep 500ms Enter
Sleep 1.5s

# List with details
Type "task-tracker list -d" Sleep 500ms Enter
Sleep 3s

# Mark task as done
Type "task-tracker mark-done 1" Sleep 500ms Enter
Sleep 1.5s

# List done tasks
Type "task-tracker list done" Sleep 500ms Enter
Sleep 2s

# Delete a task
Type "task-tracker delete 2 -d" Sleep 500ms Enter
Sleep 2s

# Final list
Type "task-tracker list" Sleep 500ms Enter
Sleep 3s

# Check version
Type "task-tracker -v" Sleep 500ms Enter
Sleep 2s
