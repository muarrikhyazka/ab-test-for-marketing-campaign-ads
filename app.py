import pandas as pd
import streamlit as st
from PIL import Image
from bokeh.models.widgets import Div
import graphviz
import base64




title = 'AB Test for Marketing Campaign Ads'


# Layout
img = Image.open('assets/icon_pink-01.png')
st.set_page_config(page_title=title, page_icon=img, layout='wide')






st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
#   width: 50%;
}
</style> """, unsafe_allow_html=True)


padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

file_name='style.css'
with open(file_name) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)






# Content
@st.cache
def load_data():
    df_control = pd.read_csv(r'data/control_group.csv', sep=';')
    df_test = pd.read_csv(r'data/test_group.csv', sep=';')
    return df_control, df_test

df_control, df_test = load_data()

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s" class="center" width="100" height="100"/>' % b64
    st.write(html, unsafe_allow_html=True)


# Sidebar color
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #ef4da0;
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    f = open("assets/icon-01.svg","r")
    lines = f.readlines()
    line_string=''.join(lines)

    render_svg(line_string)

    st.write('\n')
    st.write('\n')
    st.write('\n')

    if st.button('🏠 HOME'):
        # js = "window.location.href = 'http://www.muarrikhyazka.com'"  # Current tab
        js = "window.open('http://www.muarrikhyazka.com')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

    if st.button('🍱 GITHUB'):
        # js = "window.location.href = 'https://www.github.com/muarrikhyazka'"  # Current tab
        js = "window.open('https://www.github.com/muarrikhyazka')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)








st.title(title)

st.write(
    """
    \n
    \n
    \n
    """
)


st.subheader('Business Understanding')
st.write(
    """
    AB Test is method to take decision between two choices, its better rather than only use 'feeling' to choose. 
    Usually, AB Test used to test new/modified version with question like 'is it good enough to replace the old one or not?' or 'is there a significant difference between the two options?'
    """
)

st.write(
    """
    Problem Statement on Kaggle : 
    \n
    A company recently introduced a new bidding type, 'average bidding', as an alternative to its exisiting bidding type, called 'maximum bidding'. One of our clients, ….com, has decided to test this new feature and wants to conduct an A/B test to understand if average bidding brings more conversions than maximum bidding.
    The A/B test has run for 1 month and ….com now expects you to analyze and present the results of this A/B test.
    """
)



st.write(
    """
    In this case, we take case marketing campaign ads whether should be aired longer with better performance and spend.
    """
)

st.write(
    """
    \n
    \n
    \n
    """
)

st.subheader('Data Understanding')
st.write(
    """
    **Source : [Kaggle.](https://www.kaggle.com/datasets/ilkeryildiz/example-dataset-for-ab-test)**
    """
)

st.write(
    """
    **Below is sample of the data.** 
    """
)

st.write('Control')
st.write('The control group is exposed to the current strategy/setting of the marketing campaign ads.')
st.dataframe(df_control.sample(5))

st.write('Test/Treatment')
st.write('The test/treatment group experiences the modified or new strategy/setting of the marketing campaign ads.')
st.dataframe(df_test.sample(5))

st.write(
    """
    In here, I put the description from Kaggle of each columns which I used. I only used 4 metrics. I put the reason why I choose them on Analysis section.
    \n# of Impressions : It is a variable for the user to see an ad.
    \n# of Website Clicks : It is the variable related to the user clicking the website link in the advertisement.
    \n# of Add to Cart : It is the variable related to the user adding the product to the cart.
    \n# of Purchase : It is the variable related to the user's purchase of the product.
    """
)

st.write(
    """
    \n
    \n
    \n
    """
)

st.subheader('Method')

st.write("""
    **Flowchart**
""")

graph = graphviz.Digraph()
graph.edge('Assumption Check (Normality)', 'Assumption Check (Homogenity)')
graph.edge('Assumption Check (Homogenity)', 'Parametric Comparison (Independent Two-Sample T-Test)')
graph.edge('Assumption Check (Homogenity)', 'Nonparametric Comparison (Mann-Whitney U Test)')
graph.edge('Parametric Comparison (Independent Two-Sample T-Test)', 'Conclusion')
graph.edge('Nonparametric Comparison (Mann-Whitney U Test)', 'Conclusion')



st.graphviz_chart(graph)

st.write(
    """
    \n
    \n
    \n
    """
)


st.subheader('Analysis')
st.write(
    """
    Here, I only used 4 metrics, they are # of Impressions, # of Website Clicks, # of Add to Cart, # of Purchase. The question is Why? Because these 4 metrics represent each stage of marketing funnel :
    \n# of Impressions -> Awareness
    \n# of Website Clicks -> Interest
    \n# of Add to Cart -> Intent
    \n# of Purchase -> Purchase
    """
)

st.write(
    """
    **Assumption Check (Normality)**
    """
)

st.write(
    """
    H0 : There is no statistically significant difference between sample distribution and theoretical normal distribution
    \nH1 : There is statistically significant difference between sample distribution and theoretical normal distribution
    \n
    \nH0 is rejected if the p_value is less than 0.05.
    """
)


st.code(
    """
    Control Group 

    # of Impressions
    Test Stat = 0.9426, p-value = 0.1172 

    # of Website Clicks
    Test Stat = 0.9586, p-value = 0.3043 

    # of Add to Cart
    Test Stat = 0.9554, p-value = 0.2525 

    # of Purchase
    Test Stat = 0.9381, p-value = 0.0896 
    """
)

st.write(
    """
    All p-values are higher than 0.05 it means H0 cannot be rejected. The assumption of normality is provided.
    """
)

st.code(
    """
    Test Group 

    # of Impressions
    Test Stat = 0.9485, p-value = 0.1537 

    # of Website Clicks
    Test Stat = 0.9062, p-value = 0.0120 

    # of Add to Cart
    Test Stat = 0.9236, p-value = 0.0332 

    # of Purchase
    Test Stat = 0.9182, p-value = 0.0241 
    """
)

st.write(
    """
    # of Impressions is normal, but the rest is not
    """
)

st.write(
    """
    **Assumption Check (Homogenity)**
    """
)

st.code(
    """
    # of Impressions
    ttest statistics: 6.8867144172541295
    p_value: 0.011125294220972793

    # of Website Clicks
    ttest statistics: 0.041895271352688654
    p_value: 0.8385486753201417

    # of Add to Cart
    ttest statistics: 1.4290971599392581
    p_value: 0.2368617582504474

    # of Purchase
    ttest statistics: 1.230260648051359
    p_value: 0.2720142278811527
    """
)

st.write(
    """
    **Assumption Check (Homogenity)**
    """
)

st.write(
    """
    H0: There is no statistically significant difference between the variance of variance of the related variables of the 2 groups.
    \nH1: There is a statistically significant difference between the variance of variance of the related variables of the 2 groups.
    \n
    \nH0 is rejected if the p_value is less than 0.05.
    """
)

st.code(
    """
    # of Impressions
    ttest statistics: 6.8867144172541295
    p_value: 0.011125294220972793

    # of Website Clicks
    ttest statistics: 0.041895271352688654
    p_value: 0.8385486753201417

    # of Add to Cart
    ttest statistics: 1.4290971599392581
    p_value: 0.2368617582504474

    # of Purchase
    ttest statistics: 1.230260648051359
    p_value: 0.2720142278811527
    """
)

st.write(
    """
    All of the p values except those for the # of Impressions are higher than 0.05, 
    it means we cannot reject the H0 hypothesis. 
    Therefore, we can say that there is no statistically significant difference between the variance distributions of the # of Website Clicks,# of Add to Cart and # of Purchase values of the 2 groups.
    There is statistically significant difference between the variance distributions of the # of Impressions values of the 2 groups.
    """
)

st.write(
    """
    Metrics which fulfill homogenity assumption check will goes to Parametric Comparison (Independent Two-Sample T-Test). They are # of Website Clicks,# of Add to Cart and # of Purchase.
    The rest which is # of Impressions will goes to Nonparametric Comparison (Mann-Whitney U Test).
    """
)

st.write(
    """
    **Parametric Comparison (Independent Two-Sample T-Test)**
    """
)

st.write(
    """
    H0: µ1 = µ2 (the two population means are equal)
    \nH1: µ1 ≠ µ2 (the two population means are not equal)
    \n
    \nH0 is rejected if the p_value is less than 0.05.
    """
)

st.code(
    """
    # of Website Clicks
    ttest statistics: -1.576909404840952
    p_value: 0.12035072366063822

    # of Add to Cart
    ttest statistics: 4.24906420944249
    p_value: 8.032960071149041e-05

    # of Purchase
    ttest statistics: 0.03014479856562245
    p_value: 0.9760568756579724
    """
)

st.write(
    """
    # of Add to Cart -> the two population means are not equal
    \n# of Website Clicks, # of Purchase -> the two population means are equal
    """
)

st.write(
    """
    **Nonparametric Comparison (Mann-Whitney U Test)**
    """
)

st.write(
    """
    H0: µ1 = µ2 (the two population means are equal)
    \nH1: µ1 ≠ µ2 (the two population means are not equal)
    \n
    \nH0 is rejected if the p_value is less than 0.05.
    """
)

st.code(
    """
    # of Impressions
    ttest statistics: 697.0
    p_value: 7.344126278759323e-05
    """
)

st.write(
    """
    # of Impressions -> the two population means are not equal
    """
)

st.subheader(
    """
    Conclusion and Recommendation
    """
)

st.write(
    """
    # of Impressions : Average bidding (Test Group) has higher average.
    \n# of Website Clicks : Maximum bidding (Control Group) and Average bidding (Test Group) has the same average. 
    \n# of Add to Cart : Average bidding (Test Group) has higher average.
    \n# of Purchase : Maximum bidding (Control Group) and Average bidding (Test Group) has the same average.
    \n
    \n
    \nIf your marketing campaign ads is using Awareness (Impressions) or Intent (Add to Cart) as objective or KPI, so you should use Average bidding.
    \nIf your marketing campaign ads is using Consideration (Clicks) or Purchase (Purchase) as objective or KPI, so you should use Maximum bidding.
    """
)



c1, c2 = st.columns(2)
with c1:
    st.info('**[Github Repo](https://github.com/muarrikhyazka/ab-test-for-marketing-campaign-ads)**', icon="🍣")

