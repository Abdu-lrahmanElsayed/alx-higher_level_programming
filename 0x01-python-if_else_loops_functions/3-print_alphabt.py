#!/bin/bash/python3
print(''.join('{:c}'.format(i) for i in range(97, 123) if i not in {101, 113}))
