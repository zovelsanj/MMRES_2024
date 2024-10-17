from scipy import stats
import numpy as np

def t_test_hypothesis():
    data = [26.69284, 26.65240, 26.02918, 26.21622,
            25.93998, 27.10618, 27.51114, 25.25494]
    res=stats.ttest_1samp(data, popmean=13, alternative="two-sided") #default is two-tail
    print (f"Confidence interval: {res.confidence_interval(0.95)} \nresult statistic: {res}")
    res=stats.ttest_1samp(data, popmean=13, alternative="less") #less=>left-tail
    print (f"Confidence interval: {res.confidence_interval(0.95)} \nresult statistic: {res}")

#Example 2 (soporofic)
def lower_tail_hypothesis():
    medicine1 = np.array([0.7,-1.6,-0.2,-1.2,-0.1,3.4,3.7,0.8,0,2])
    medicine2 = np.array([1.9,0.8,1.1,0.1,-0.1,4.4,5.5,1.6,4.6,3.4])

    x = medicine2-medicine1
    res=stats.ttest_1samp(x, popmean=0, alternative='greater') #greater=>right-tail
    print (f"Confidence interval: {res.confidence_interval(0.95)} \nresult statistic: {res}")

    #Alternativelys
    t_statistic, p_value = stats.ttest_rel(medicine2, medicine1, alternative='greater')
    print(f"t_statistic: {t_statistic}, p-value: {p_value}")

if __name__=="__main__":
    # t_test_hypothesis()
    lower_tail_hypothesis()