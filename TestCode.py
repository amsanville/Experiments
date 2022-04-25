# Test python code
# This file is meant to allow me to test various snippets of python where 
# googling is a pain in the ass and I just want an answer now.


class A():
    field1 = 'default value'

def main():
    # First test is to see how class field values behave
    print('Test 1: Class Default Copy Method')
    test1_1 = A()
    test1_1.field1 = 'not default'
    test1_2 = A()
    print('Values in test classes:')
    print('1.1:', test1_1.field1)
    print('1.2:', test1_2.field1)
    test1_2 = test1_1
    print('Post Copy')
    print('1.2 (should be copy of 1.1):', test1_2)
    test1_1.field1 = 'changed value'
    print('Changing 1.1:')
    print('1.1:', test1_1.field1)
    print('1.2:', test1_2.field1)
    # Conclusion: pass by reference



if __name__ == '__main__':
    main()