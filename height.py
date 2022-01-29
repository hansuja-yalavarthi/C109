import pandas as  pd
import statistics
import csv

df=pd.read_csv("height-weight.csv")
height=df["Height(Inches)"].to_list()
weight=df["Weight(Pounds)"].to_list()
height_mean=statistics.mean(height)
weight_mean=statistics.mean(weight)
height_median=statistics.median(height)
weight_median=statistics.median(weight)
height_mode=statistics.mode(height)
weight_mode=statistics.mode(weight)
print("mean, median, and mode of height is {}, {}, and {}".format(height_mean, height_median, height_mode))
print("mean, median, and mode of weight is {}, {}, and {}".format(weight_mean, weight_median, weight_mode))
height_stdev=statistics.stdev(height)
weight_stdev=statistics.stdev(weight)
height_first_stdev_start, height_first_stdev_end = height_mean - height_stdev, height_mean + height_stdev
height_second_stdev_start, height_second_stdev_end = height_mean - (2* height_stdev), height_mean + (2* height_stdev)
height_third_stdev_start, height_third_stdev_end = height_mean - (3* height_stdev), height_mean + (3* height_stdev)
weight_first_stdev_start, weight_first_stdev_end = weight_mean - weight_stdev, weight_mean + weight_stdev
weight_second_stdev_start, weight_second_stdev_end = weight_mean - (2* weight_stdev), weight_mean + (2* weight_stdev)
weight_third_stdev_start, weight_third_stdev_end = weight_mean - (3* weight_stdev), weight_mean + (3* weight_stdev)
height_data_1stdev=[result for result in height if result > height_first_stdev_start and result < height_first_stdev_end]
height_data_2stdev=[result for result in height if result > height_second_stdev_start and result < height_second_stdev_end]
height_data_3stdev=[result for result in height if result > height_third_stdev_start and result < height_third_stdev_end]
weight_data_1stdev=[result for result in weight if result > weight_first_stdev_start and result < weight_first_stdev_end]
weight_data_2stdev=[result for result in weight if result > weight_second_stdev_start and result < weight_second_stdev_end]
weight_data_3stdev=[result for result in weight if result > weight_third_stdev_start and result < weight_third_stdev_end]
print("{} % of data for height within 1 stdev".format(len(height_data_1stdev)*100.0/len(height)))
print("{} % of data for height within 2 stdev".format(len(height_data_2stdev)*100.0/len(height)))
print("{} % of data for height within 3 stdev".format(len(height_data_3stdev)*100.0/len(height)))
print("{} % of data for weight within 1 stdev".format(len(weight_data_1stdev)*100.0/len(weight)))
print("{} % of data for weight within 2 stdev".format(len(weight_data_2stdev)*100.0/len(weight)))
print("{} % of data for weight within 3 stdev".format(len(weight_data_3stdev)*100.0/len(weight)))