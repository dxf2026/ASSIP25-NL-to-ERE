1. create files ground_truth_ere.txt, generated_ere.txt
2. ground_truth_ere.txt contains the following format
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
4. Run standardizer.py with the following parameters, in the following order
```python
python standardizer.py generated_ere.txt ground_truth_ere.txt
```
