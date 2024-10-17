from bioinfokit.analys import stat
from scipy import stats
import pandas as pd

def one_sample_z_test():
    data = {'x': [13.34642, 13.32620, 13.01459, 13.10811, 12.96999, 13.55309, 13.75557, 12.62747]}
    df = pd.DataFrame(data)
    res = stat()
    res.ztest(df=df, x='x', mu=13, x_std=0.35, test_type=1)
    print(res.summary)

def one_sample_t_test():
    x = [64.1,64.7,64.5,64.6,64.5,64.3,64.6,64.8,64.2,64.3]
    res = stats.ttest_1samp(x, popmean=0) #population mean=0
    res.confidence_interval(confidence_level=0.95)
    print(res.confidence_interval())

if __name__=="__main__":
    one_sample_z_test()
    one_sample_t_test()
