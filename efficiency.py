import timeit
import argparse


lon1,lat1,lon2,lat2=-72.345,34.323,-61.823,54.826
num = 500000

def time2():
    t = timeit.Timer('v2.great_circle(%f,%f,%f,%f)' % (lon1,lat1,lon2,lat2),
        'import version2 as v2')

    print('v2 ---> cost {} sec'.format(t.timeit(num)))

def time1():
    t = timeit.Timer('v1.great_circle(%f,%f,%f,%f)' % (lon1,lat1,lon2,lat2),
        'import version1 as v1')

    print('v1 ---> cost {} sec'.format(t.timeit(num)))

def time3():
    t = timeit.Timer('v3.great_circle(%f,%f,%f,%f)' % (lon1,lat1,lon2,lat2),
        'import version3 as v3')

    print('v3 ---> cost {} sec'.format(t.timeit(num)))

def time4():
    t = timeit.Timer('v4.great_circle(%f,%f,%f,%f,%i)' % (lon1,lat1,lon2,lat2,num),
        'import version4 as v4')

    print('v4 ---> cost {} sec'.format(t.timeit(1)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--c',type=int)
    args = parser.parse_args()
    choice = args.c
    if choice == 1:
        time1()
    elif choice == 2:
        time2()
    elif choice == 3:
        time3()
    elif choice == 4:
        time4()
    else:
        print('wrong choice!')