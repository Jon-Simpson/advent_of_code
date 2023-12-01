import pandas as pd


def get_first_and_last_numbers(string: str):
    nums = []
    for i in string:
        try:
            num = int(i)
            nums.append(num)
        except:
            pass
    return int(str(nums[0]) + str(nums[-1]))


if __name__ == "__main__":

    df = pd.read_csv('/Users/jonsimpson/Downloads/input.csv', header=None)
    print(
        sum(df.iloc[:,0].apply(get_first_and_last_numbers))
    )
