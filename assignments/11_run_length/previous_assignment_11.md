(.venv) lazuline@Lazuline-LAPTOP:~/be434-spring-2023/assignments/11_run_length$ ls -alh
total 48K
drwxr-xr-x  6 lazuline lazuline 4.0K Apr 12 14:43 .
drwxr-xr-x 15 lazuline lazuline 4.0K Mar  4 06:54 ..
drwxr-xr-x  3 lazuline lazuline 4.0K Apr 12 12:30 .pytest_cache
-rw-r--r--  1 lazuline lazuline   63 Jan 19 07:46 Makefile
-rw-r--r--  1 lazuline lazuline 5.9K Feb 16 12:05 README.md
drwxr-xr-x  2 lazuline lazuline 4.0K Apr 12 14:43 __pycache__
drwxr-xr-x  2 lazuline lazuline 4.0K Jan 19 07:46 expected
drwxr-xr-x  2 lazuline lazuline 4.0K Jan 19 07:46 inputs
-rwxr-xr-x  1 lazuline lazuline  421 Jan 19 07:46 mk-outs.sh
-rwxr-xr-x  1 lazuline lazuline 2.6K Apr 12 14:43 run.py
-rwxr-xr-x  1 lazuline lazuline 2.0K Jan 19 07:46 test.py
(.venv) lazuline@Lazuline-LAPTOP:~/be434-spring-2023/assignments/11_run_length$ make test
pytest -xv test.py run.py
======================================================== test session starts ========================================================
platform linux -- Python 3.11.0rc1, pytest-7.2.1, pluggy-1.0.0 -- /home/lazuline/be434-spring-2023/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/lazuline/be434-spring-2023/assignments/11_run_length
plugins: mypy-0.10.3, pylint-0.19.0, flake8-1.1.1
collected 10 items                                                                                                                  

test.py::test_exists PASSED                                                                                                   [ 10%]
test.py::test_usage PASSED                                                                                                    [ 20%]
test.py::test1 PASSED                                                                                                         [ 30%]
test.py::test2 PASSED                                                                                                         [ 40%]
test.py::test3 PASSED                                                                                                         [ 50%]
test.py::test4 PASSED                                                                                                         [ 60%]
test.py::test5 PASSED                                                                                                         [ 70%]
test.py::test_sample1 PASSED                                                                                                  [ 80%]
test.py::test_sample2 PASSED                                                                                                  [ 90%]
test.py::test_sample3 PASSED                                                                                                  [100%]

======================================================== 10 passed in 0.30s =========================================================
flake8 run.py
pylint run.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

(.venv) lazuline@Lazuline-LAPTOP:~/be434-spring-2023/assignments/11_run_length$ 
