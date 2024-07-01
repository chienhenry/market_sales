# 第十章/add_key_text.py
import pandas as pd
import streamlit as st


def get_dataframe_from_excel():
    # pd.read_excel()函数用于读取Excel文件的数据
    # 'supermarket_sales.xlsx'表示Excel文件的路径及名称
    # sheet_name='销售数据'表示读取名为“销售数据”的工作表的数据
    # skiprows=1表示跳过 Excel中的第一行,因为第一行是标题
    # index_col='订单号'表示将“订单号”这一列作为返回的数据框的索引
    # 最后将读取到的数据框赋值给变量df

    df = pd.read_excel('supermarket_sales.xlsx',
                        sheet_name='销售数据',
                        skiprows=1,
                        index_col='订单号'
                        )
    # df['时间']取出原有的'时间'这一列,其中包含交易的完整时间字符串,如'10:25:30'
    # pd.to_datetime将'时间'列转换成datetime类型
    # format="%H:%M:%S"指定了原有时间字符串的格式
    # .dt.hour表示从转换后的数据框取出小时数作为新列
    # 最后赋值给sale_df['小时'],就得到了一个包含交易小时的新列。
    df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour
    return df


def add_sidebar_func(df):
    # 创建侧边栏
    with st.sidebar:
        # 添加侧边栏标题
        st.header("请筛选数据：")
        # 求数据框“城市”列去重复后值，赋值给city_unique
        city_unique = df["城市"].unique()
        city = st.multiselect(
            "请选择城市：",
            options=city_unique,  # 设置所有选项为city_unique
            default=city_unique,   # 第一次的默认选项为city_unique
        )
        # 求数据框“顾客类型”列去重复后值，赋值给customer_type_unique
        customer_type_unique = df["顾客类型"].unique()
        customer_type = st.multiselect(
            "请选择顾客类型：",
            options=customer_type_unique, # 设置所有选项为customer_type_unique
            default=customer_type_unique, # 第一次的默认选项为customer_type_unique
        )
        # 求数据框“性别”列去重复后值，赋值给gender_unique
        gender_unique = df["性别"].unique()
        gender = st.multiselect(
            "请选择性别",
            options=gender_unique,   # 设置所有选项为gender_unique
            default=gender_unique,  # 第一次的默认选项为gender_unique
        )
        # query():查询方法,传入过滤条件字符串
        # @city: 通过@可以使用Streamlit多选下拉按钮“城市”的值
        # @customer_type:通过@可以使用Streamlit多选下拉按钮“顾客类型”的值
        # @gender:通过@可以使用Streamlit多选下拉按钮“性别”的值
        # 最后赋值给变量df_selection
        df_selection = df.query(
            "城市 == @city & 顾客类型 ==@customer_type & 性别 == @gender"
        )

        return df_selection
# 读取excel中的销售数据到数据框中
sale_df = get_dataframe_from_excel()
# 添加不同的多选下拉按钮，并形成筛选后的数据框
df_selection = add_sidebar_func(sale_df)
# 选中的数据框中的"总价"列，使用sum()计算"总价"列的和，使用int()求整
total_sales = int(df_selection["总价"].sum())
# 选中的数据框中的"评分"列，使用mean()计算"评分"列的平均值，使用round()四舍五入，保留一位小数
average_rating = round(df_selection["评分"].mean(), 1)
# 对刚刚的结果再次四舍五入，只保留整数，并使用int()函数，表示就要整数，增加代码的可读性
star_rating_string = ":star:" * int(round(average_rating, 0))
# 选中的数据框中的"总价"列，使用mean()计算"总价"列的平均值，使用round()四舍五入，保留二位小数
average_sale_by_transaction = round(df_selection["总价"].mean(), 2)

st.subheader("总销售额：")
st.subheader(f"RMB ￥ {total_sales:,}")
# 使用三个“-”在markdown语法下会生成分割的横线
st.markdown('---')

st.subheader("顾客评分的平均值：")
st.subheader(f"{average_rating} {star_rating_string}")
# 同样产生分割的横线
st.divider()

st.subheader("每单的平均销售额:")
st.subheader(f"RMB ￥ {average_sale_by_transaction}")
