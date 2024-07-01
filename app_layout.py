# 第十章/app_layout.py
import streamlit as st

def sidebar_demo():
    """筛选区函数"""
    # 创建侧边栏
    with st.sidebar:
        # 添加侧边栏标题
        st.header("模拟筛选区")
        city = st.multiselect(
            "请选择城市：",
            options=['太原', '临汾'],
            default=['临汾'],
        )

def main_page_demo():
    """主界面函数"""
    # 设置标题
    st.title(':bar_chart:销售仪表板')
    # 创建关键指标信息区，生成三个列容器
    left_key_col, middle_key_col, right_key_col = st.columns(3)

    with left_key_col:
        st.subheader("关键指标信息1")
        st.markdown("具体信息1")

    with middle_key_col:
        st.subheader("关键指标信息2")
        st.markdown("具体信息2")

    with right_key_col:
        st.subheader("关键指标信息3")
        st.markdown("具体信息3")

    st.divider()  # 生成一个水平分割线

    # 创建图表信息区，生成2个列容器
    left_chart_col, right_chart_col = st.columns(2)
    with left_chart_col:
        st.subheader("图表1")
        st.markdown("具体信息图表1")

    with right_chart_col:
        st.subheader("图表2")
        st.markdown("具体信息图表2")

def run_app():
    """启动应用"""
    # 设置页面
    st.set_page_config(
        page_title="销售仪表板",  # 标题
        page_icon=":bar_chart:",  # 图标
        layout="wide"  # 宽布局
        )
    # 调用筛选区函数
    sidebar_demo()
    # 调用主界面函数
    main_page_demo()




# 标准的python程序开始
if __name__ == "__main__":
    run_app()
