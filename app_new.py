import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from analyzer import AdvancedSupplyChainAnalyzer

# Page Configuration
st.set_page_config(
    page_title="Supply Chain Analytics Dashboard",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern light theme
st.markdown("""
    <style>
    /* Base theme colors and variables */
    :root {
        /* Primary colors */
        --primary-color: #60a5fa;
        --primary-light: #93c5fd;
        --primary-dark: #3b82f6;
        
        /* Layout colors */
        --background-color: #0f172a;
        --surface-color: #1e293b;
        --border-color: #334155;
        
        /* Layout spacing */
        --content-padding: 1.5rem;
        --grid-gap: 1rem;
        --section-spacing: 2rem;
        
        /* Text colors */
        --text-color: #f8fafc;
        --text-secondary-color: #cbd5e1;
        --text-muted: #94a3b8;
        
        /* Accent colors */
        --accent-color: #38bdf8;
        --accent-light: #7dd3fc;
        
        /* Status colors */
        --success-color: #4ade80;
        --warning-color: #fbbf24;
        --error-color: #f87171;
        
        /* Card and surface colors */
        --metric-bg-color: #1e293b;
        --card-hover-bg: #334155;
        
        /* Shadows */
        --card-shadow: rgba(0, 0, 0, 0.25) 0px 1px 3px, rgba(0, 0, 0, 0.15) 0px 1px 2px;
        --hover-shadow: rgba(0, 0, 0, 0.35) 0px 4px 12px, rgba(0, 0, 0, 0.25) 0px 2px 4px;
        
        /* Chart colors */
        --chart-color-1: #60a5fa;
        --chart-color-2: #4ade80;
        --chart-color-3: #fbbf24;
        --chart-color-4: #f87171;
        --chart-color-5: #c084fc;
    }

    /* Dashboard containers and charts */
    div[data-testid="stPlotlyChart"], 
    div.stGraph,
    .chart-container {
        background: var(--surface-color);
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid var(--border-color);
        margin: 1rem 0;
        box-shadow: var(--card-shadow);
        min-height: 300px;
        height: auto !important;
        width: 100% !important;
        transition: all 0.2s ease-in-out;
        margin-bottom: 2rem;
    }

    div[data-testid="stPlotlyChart"]:hover, 
    div.stGraph:hover,
    .chart-container:hover {
        box-shadow: var(--hover-shadow);
        border-color: var(--primary-light);
    }

    /* Force plotly chart visibility */
    .plotly-graph-div,
    .js-plotly-plot,
    .plot-container,
    .plotly,
    [class*="View"] {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    .stApp {
        background: var(--background-color);
    }
    
    .main .block-container {
        padding: 2rem;
        max-width: 95%;
        margin: 0 auto;
    }
    
    /* Add spacing between sections */
    .element-container {
        margin-bottom: 2rem !important;
    }
    
    /* Table/DataFrame styling */
    .stDataFrame {
        font-size: 1.1rem !important;
        border-radius: 0.5rem !important;
        overflow: hidden !important;
        border: 1px solid var(--border-color) !important;
        background: var(--surface-color) !important;
    }
    
    div[data-testid="stTable"] th {
        font-weight: 600 !important;
        background-color: var(--surface-color) !important;
        color: var(--text-color) !important;
        border-bottom: 2px solid var(--border-color) !important;
        padding: 1rem !important;
    }
    
    div[data-testid="stTable"] td {
        color: var(--text-secondary-color) !important;
        border-bottom: 1px solid var(--border-color) !important;
        padding: 0.75rem 1rem !important;
    }
    
    div[data-testid="stTable"] tr:hover {
        background-color: var(--card-hover-bg) !important;
    }

    /* Metric container styling */
    div[data-testid="metric-container"] {
        background-color: var(--surface-color);
        border: 1px solid var(--border-color);
        padding: 1.5rem;
        border-radius: 0.75rem;
        width: 100%;
        box-shadow: var(--card-shadow);
        transition: all 0.2s ease-in-out;
    }

    div[data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        box-shadow: var(--hover-shadow);
        border-color: var(--primary-color);
        background-color: var(--card-hover-bg);
    }

    div[data-testid="metric-container"] > div:first-child {
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--text-secondary-color);
        margin-bottom: 0.5rem;
    }

    div[data-testid="metric-container"] > div:nth-child(2),
    div[data-testid="stMetricValue"] {
        font-size: 2.4rem !important;
        font-weight: 700 !important;
        color: var(--text-color) !important;
        line-height: 1.2 !important;
        margin: 0.5rem 0 !important;
        opacity: 1 !important;
    }

    /* Metric delta styling */
    div[data-testid="stMetricDelta"] {
        font-size: 1.2rem !important;
    }

    div[data-testid="stMetricDelta"] > div {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: flex-start !important;
        gap: 0.2rem !important;
        color: var(--text-color) !important;
        opacity: 1 !important;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(to right, var(--primary-color), var(--primary-dark)) !important;
        color: var(--background-color) !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        border-radius: 0.5rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover {
        filter: brightness(110%) !important;
        box-shadow: 0 0 15px rgba(96, 165, 250, 0.3) !important;
    }

    /* Chart and container adjustments for dark theme */
    div[data-testid="stPlotlyChart"], 
    div.stGraph,
    .chart-container {
        background: var(--surface-color);
        border: 1px solid var(--border-color);
        box-shadow: var(--card-shadow);
    }

    /* Sidebar styling */
    .stSidebar [data-testid="stSidebarNav"] {
        background-color: var(--surface-color);
        border-right: 1px solid var(--border-color);
    }

    .stSidebar .stRadio > div {
        background-color: var(--surface-color);
        border: 1px solid var(--border-color);
    }

    .stSidebar .stRadio > div:hover {
        background-color: var(--card-hover-bg);
        border-color: var(--primary-color);
    }

    /* Search input styling */
    .stTextInput > div > div > input {
        background-color: var(--surface-color);
        border: 1px solid var(--border-color);
        color: var(--text-color);
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.2);
    }

    /* Select box styling */
    .stSelectbox > div > div {
        background-color: var(--surface-color);
        border: 1px solid var(--border-color);
        color: var(--text-color);
    }

    .stSelectbox > div > div:hover {
        border-color: var(--primary-color);
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab"] {
        color: var(--text-secondary-color);
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: var(--primary-color);
        background-color: var(--card-hover-bg);
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: var(--primary-color);
        border-bottom-color: var(--primary-color);
        background-color: var(--card-hover-bg);
    }

    /* Warning message styling */
    .stAlert {
        background-color: var(--surface-color);
        color: var(--text-color);
        border: 1px solid var(--border-color);
    }

    /* Plotly chart adjustments */
    .js-plotly-plot .plotly {
        background-color: var(--surface-color) !important;
    }

    .js-plotly-plot .plot-container {
        color: var(--text-color) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state and load data
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = AdvancedSupplyChainAnalyzer()
    with st.spinner("Loading analytics..."):
        st.session_state.analyzer.generate_realistic_data()
        st.session_state.analyzer.calculate_advanced_metrics()

analyzer = st.session_state.analyzer
data = analyzer.get_supply_chain_data()

# Process date/year information once
if 'Date' in data.columns:
    data['Year'] = pd.to_datetime(data['Date']).dt.year
elif 'Month' in data.columns:
    data['Year'] = pd.to_datetime(data['Month']).dt.year

# Sidebar configuration
with st.sidebar:
    st.markdown("""
        <div style='padding: 1rem 0;'>
            <h2 style='color: var(--text-color); font-size: 1.5rem; font-weight: 600; margin: 0;'>Supply Chain Analytics</h2>
        </div>
    """, unsafe_allow_html=True)
    
    selected_dashboard = st.radio(
        "### Dashboards",
        ["Supplier Analytics", "Supply Chain Performance", "Risk Management"],
        label_visibility="collapsed"
    )
    
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    
    current_year = pd.Timestamp.now().year
    selected_year = st.selectbox(
        "### Time Period",
        options=range(current_year-2, current_year+1),
        index=2,
        help="Select year for analysis"
    )
    
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    if st.button("📊 Export Dashboard", use_container_width=True):
        st.download_button(
            label="Download Report",
            data=analyzer.export_report(),
            file_name=f"supply_chain_report_{selected_year}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Filter data for selected year
filtered_data = data[data['Year'] == selected_year].copy()

# Aggregate metrics if needed
if 'Annual_Volume_USD' in filtered_data.columns and 'Total_Volume_USD' not in filtered_data.columns:
    filtered_data['Total_Volume_USD'] = filtered_data['Annual_Volume_USD']

required_columns = ['Category', 'Total_Volume_USD', 'Overall_Performance_Score', 'Supply_Risk_Score']
if all(col in filtered_data.columns for col in required_columns):
    filtered_data = filtered_data.groupby(['Supplier_Name', 'Category'])[
        ['Total_Volume_USD', 'Overall_Performance_Score', 'Supply_Risk_Score']
    ].agg({
        'Total_Volume_USD': 'sum',
        'Overall_Performance_Score': 'mean',
        'Supply_Risk_Score': 'mean'
    }).reset_index()

# Main dashboard header with enhanced card design
st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, var(--surface-color), var(--card-hover-bg));
        border: 1px solid var(--border-color);
        border-radius: 1rem;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: var(--card-shadow);
        position: relative;
        overflow: hidden;
    '>
        <div style='
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
        '></div>
        <h1 style='
            color: var(--text-color);
            font-size: 2.2rem;
            font-weight: 700;
            margin: 0;
            display: flex;
            align-items: center;
            gap: 1rem;
        '>
            <span style='
                background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            '>{selected_dashboard}</span>
        </h1>
        <p style='
            color: var(--text-secondary-color);
            font-size: 1.1rem;
            margin: 1rem 0 0 0;
        '>Comprehensive analytics and insights for your supply chain management</p>
    </div>
""", unsafe_allow_html=True)

# SINGLE ROW OF METRICS - Using Streamlit's built-in metrics
if selected_dashboard == "Supplier Analytics":
    # Calculate metrics
    total_suppliers = filtered_data['Supplier_Name'].nunique()
    total_spend = filtered_data['Total_Volume_USD'].sum()
    avg_performance = filtered_data['Overall_Performance_Score'].mean()
    avg_risk = filtered_data['Supply_Risk_Score'].mean()
    
    # Display in a single row using columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Suppliers",
            value=total_suppliers,
            delta=analyzer.get_supplier_growth() if hasattr(analyzer, 'get_supplier_growth') else None
        )
    
    with col2:
        st.metric(
            label="Total Spend",
            value=f"${total_spend:,.0f}",
            delta=f"{analyzer.get_volume_growth()}" if hasattr(analyzer, 'get_volume_growth') else None
        )
    
    with col3:
        st.metric(
            label="Avg. Performance",
            value=f"{avg_performance:.1f}%",
            delta=f"{analyzer.get_performance_change()}" if hasattr(analyzer, 'get_performance_change') else None
        )
    
    with col4:
        st.metric(
            label="Avg. Risk Score",
            value=f"{avg_risk:.1f}",
            delta=f"{analyzer.get_risk_change()}" if hasattr(analyzer, 'get_risk_change') else None,
            delta_color="inverse"  # Lower risk is better
        )

# Add spacing
st.markdown("<hr style='margin: 2rem 0; opacity: 0.2;'>", unsafe_allow_html=True)

# Dashboard tabs
tab1, tab2, tab3 = st.tabs(["Performance Overview", "Detailed Analysis", "Strategic Insights"])

with tab1:
   
    
    # Create container for the chart using columns
    st.markdown("<div style='margin: 4rem 0;'>", unsafe_allow_html=True)
    container = st.container()
    with container:
        fig = analyzer.create_modern_dashboard(filtered_data)
        # Update figure layout with more breathing room
        fig.update_layout(
            height=900,  # Increased height for better visibility
            margin=dict(t=100, l=70, r=70, b=120),  # Increased margins all around
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,  # Moved legend down
                xanchor="center",
                x=0.5
            )
        )
        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                'displayModeBar': True,
                'displaylogo': False,
                'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d'],
                'responsive': True
            }
        )
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add substantial spacing between charts
    st.markdown("<div style='height: 6rem;'></div>", unsafe_allow_html=True)
    
    # Volume distribution
    st.markdown("""
        <div style='margin: 3rem 0 1.5rem 0;'>
            <h3 style='color: var(--text-color); font-size: 1.3rem; font-weight: 600;'>Volume Distribution by Category</h3>
            <p style='color: var(--text-secondary-color); margin-top: 0.5rem; font-size: 0.9rem;'>Distribution of total volume across different categories</p>
        </div>
    """, unsafe_allow_html=True)
    if 'Total_Volume_USD' in filtered_data.columns:
        volume_data = filtered_data.groupby('Category')['Total_Volume_USD'].sum().reset_index()
        volume_fig = analyzer.create_volume_chart(volume_data)
        # Update volume chart layout with more spacing
        volume_fig.update_layout(
            height=500,  # Increased height
            margin=dict(t=80, l=70, r=70, b=100),  # Larger margins for better spacing
            title=None,  # Remove title as we have it in the markdown
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
            plot_bgcolor='rgba(0,0,0,0)'  # Transparent plot area
        )
        st.markdown("<div style='margin: 2rem 0;'>", unsafe_allow_html=True)
        st.plotly_chart(
            volume_fig,
            use_container_width=True,
            config={'displayModeBar': False}
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Add extra spacing after the volume chart
        st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    else:
        st.warning("Volume data is not available. Please ensure the data is fully loaded.")

# Add detailed data table with increased spacing
st.markdown("<div style='height: 5rem;'></div>", unsafe_allow_html=True)
st.markdown("""
    <div style='margin: 3rem 0 2rem 0;'>
        <h3 style='color: var(--text-color); font-size: 1.2rem; font-weight: 600;'>Detailed Supply Chain Data</h3>
        <p style='color: var(--text-secondary-color); margin-top: 0.5rem; font-size: 0.9rem;'>Comprehensive view of all supplier metrics</p>
    </div>
""", unsafe_allow_html=True)

# Add search and filter options
search = st.text_input("🔍 Search Suppliers")
if search:
    filtered_data = filtered_data[
        filtered_data['Supplier_Name'].str.contains(search, case=False) |
        filtered_data['Category'].str.contains(search, case=False)
    ]

# Display the filtered data in a modern table with styling
styled_df = filtered_data[[
    'Supplier_Name', 'Category', 'Total_Volume_USD',
    'Overall_Performance_Score', 'Supply_Risk_Score'
]].copy()

# Add styling
styled_df = styled_df.style\
    .format({
        'Total_Volume_USD': '${:,.2f}',
        'Overall_Performance_Score': '{:.1f}%',
        'Supply_Risk_Score': '{:.1f}'
    })\
    .background_gradient(
        subset=['Overall_Performance_Score'], 
        cmap='RdYlGn',
        vmin=0,
        vmax=100
    )\
    .background_gradient(
        subset=['Supply_Risk_Score'],
        cmap='RdYlGn_r',
        vmin=0,
        vmax=100
    )

st.dataframe(
    styled_df,
    use_container_width=True,
    height=350  # Slightly reduced height
)

with tab2:
    st.markdown("""
        <div style='margin: 0.5rem 0 1rem 0;'>
            <h2 style='color: var(--text-color); font-size: 1.4rem; font-weight: 600;'>Detailed Analysis</h2>
            <p style='color: var(--text-secondary-color); margin-top: 0.25rem; font-size: 0.9rem;'>In-depth analysis of supplier performance and distribution</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Risk Analysis Matrix
    st.markdown("""
        <div style='margin: 0.5rem 0;'>
            <h3 style='color: var(--text-color); font-size: 1.2rem; font-weight: 600;'>Risk Assessment</h3>
            <p style='color: var(--text-secondary-color); margin-top: 0.25rem; font-size: 0.9rem;'>Performance vs Risk analysis of suppliers</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Prepare risk matrix data
    risk_matrix = filtered_data[['Supplier_Name', 'Overall_Performance_Score', 'Supply_Risk_Score', 'Total_Volume_USD']].copy()
    risk_matrix['Bubble_Size'] = risk_matrix['Total_Volume_USD'].apply(lambda x: max(10, min(60, x/100000)))
    
    risk_fig = analyzer.create_risk_matrix(risk_matrix)
    risk_fig.update_layout(
        height=450,  # Reduced height
        margin=dict(t=20, l=50, r=50, b=50),  # Tighter margins
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255, 255, 255, 0.05)',
            bordercolor='rgba(255, 255, 255, 0.2)'
        )
    )
    st.plotly_chart(
        risk_fig,
        use_container_width=True,
        config={'displayModeBar': False}
    )

with tab3:
    st.markdown("""
        <div style='margin: 0.5rem 0 1rem 0;'>
            <h2 style='color: var(--text-color); font-size: 1.4rem; font-weight: 600;'>Strategic Insights</h2>
            <p style='color: var(--text-secondary-color); margin-top: 0.25rem; font-size: 0.9rem;'>Key findings and actionable recommendations</p>
        </div>
    """, unsafe_allow_html=True)
    
    insights = analyzer.generate_strategic_insights()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div style='margin-bottom: 0.5rem;'>
                <h3 style='color: var(--text-color); font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;'>Executive Summary</h3>
                <p style='color: var(--text-secondary-color); font-size: 0.9rem; margin-bottom: 0.5rem;'>High-level performance overview</p>
            </div>
        """, unsafe_allow_html=True)
        summary_df = pd.DataFrame(insights['Executive Summary'].items(), columns=['Metric', 'Value'])
        st.dataframe(summary_df, hide_index=True, use_container_width=True, height=200)
    
    with col2:
        st.markdown("""
            <div style='margin-bottom: 0.5rem;'>
                <h3 style='color: var(--text-color); font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;'>Key Recommendations</h3>
                <p style='color: var(--text-secondary-color); font-size: 0.9rem; margin-bottom: 0.5rem;'>Strategic action items</p>
            </div>
        """, unsafe_allow_html=True)
        st.dataframe(pd.DataFrame(insights['Key Recommendations']), hide_index=True, use_container_width=True)