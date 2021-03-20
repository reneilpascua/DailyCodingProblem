# Daily Coding Problem

Problems from https://www.dailycodingproblem.com/, they send one to your email every day.

Repo of my attempts to solve the daily problem, using Python 3.7.4. I don't have the premium version so I don't have the solutions. I'm not sure if they provide a set of test cases.

### Coming Soon
A way to test, given many inputs and expected outputs in the template solution file.

### Getting Started
1. Optional: Create a virtual environment and activate it

    create: ```python -m venv venv```
    activate:```source ./venv/bin/activate```

2. ```pip install numpy``` or ```pip install -r requirements.txt``` if there are other libs

    some solutions might use numpy, although usually you would try to solve a coding problem without extra libs.

3. Must be inside ./problems when you run the python files, or else importing helpers module won't work.

### VS Code
If you're using VS Code, in .vscode/launch.json, ensure your cwd uses '${fileDirname}' so that it runs in the containing folder so imports will work. This helps to use debug facilities.
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "cwd": "${fileDirname}",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```