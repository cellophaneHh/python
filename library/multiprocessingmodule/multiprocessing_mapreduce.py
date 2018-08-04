import collections
import itertools
import multiprocessing


class SimpleMapReduce:

    def __init__(self, map_func, reduce_func, num_workers=None):

        '''
        map_func

          将输入转换为中间数据，接受一个输入并返回一个元组

        reduce_func

          化简、分割中间结构的数据到最终输出，接受一个被map_func返回的key和一个关联此key的序列

        num_workers

          池中创建的工作者数量，默认是当前及其的cpu数
        '''
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        '''
        '''
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        '''
        处理map和reduce传递的输入
        inputs
          可迭代的输入数据
        chunksize=1
          每个worker处理的输入数据数量
        '''
        map_responses = self.pool.map(
            self.map_func,
            inputs,
            chunksize=chunksize,
        )
        partitioned_data = self.partition(
            itertools.chain(*map_responses)
        )
        reduced_values = self.pool.map(
            self.reduce_func,
            partitioned_data,
        )
        return reduced_values
