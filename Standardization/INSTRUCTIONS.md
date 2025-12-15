1. create files ground_truth_ere.txt, generated_ere.txt
2. ground_truth_ere.txt contains the following format. Match or fail depends on the file, same with which events are labeled as creation
```cpp
gt_ere1;match;creation_event1,creation_event2,...
gt_ere2;fail;creation_event1,creation_event2,...
gt_ere3;fail;creation_event1,creation_event2,...
.
.
.
```
3. generated_ere.txt contains the following format
```cpp
gen_ere1
gen_ere2
gen_ere3
.
.
.
```
4. run standardizer.py with the following parameters, in the following order
```python
python standardizer.py generated_ere.txt ground_truth_ere.txt
```
5. output will be the following format in the std output stream, True/False depends on result
```python
Test #0:
Ground: gt_ere1
Generated: gen_ere1
Result: True

Test #1:
Ground: gt_ere2
Generated: gen_ere2
Result: False

Test #2:
Ground: gt_ere3
Generated: gen_ere3
Result: False
.
.
.
Driver Closed, Finished Tests
```
