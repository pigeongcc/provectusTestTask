# Level 1 Exercise Readme

### How To Run

You can run the script by calling

```python
level1.match_users_to_images(working_dir_path)
```
`working_dir_path` is the path to the **"working directory"**. Working directory contains `src-data` folder.
The script will create some files in working directory while executing.

### Details

* Comments in the code explain how the script works
* Updatability is supported. For this purpose, the script saves a `user_dict` dictionary to .pkl file. This file is a database prototype. The script tries to access this file every execution. If it cannot find `user_dict.pkl`, it creates a new one in the working directory.
* Paths in the script are supposed to be OS-independent.
