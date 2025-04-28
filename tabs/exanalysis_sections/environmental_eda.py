import streamlit as st

try:
    from scripts.visualization import plot_time_series, plot_time_series_double, plot_correlation_heatmap, other_visualize

except ImportError as e:
    st.error(f"Failed to import modules: {e}")
    st.stop()


def show():
    st.write("""
    This section includes the exploration of glacier data overview for Nepal.
    """)
    
    # Data preview
    st.subheader("Data Preview")

    if "glacierdf" in st.session_state:
        glacierdf = st.session_state.glacierdf
    else:
        st.error("Data not loaded. Please go to the overview and load again.")

    glacierdf = st.session_state.glacierdf

    st.dataframe(glacierdf, height=200)

    st.divider()
    
    st.subheader("DataFrame Info")
    st.write(f"Data shape: {glacierdf.shape[0]} Rows, {glacierdf.shape[1]} Columns")

    # Grid layout: Three columns
    col1, col2 = st.columns(2)

    
    with col1:
        st.write("Data types:", glacierdf.dtypes)

    with col2:
        st.write("Missing values:", glacierdf.isnull().sum())


    st.divider()
    st.subheader("DataFrame Statistical Description")
    st.dataframe(glacierdf.describe())
    st.divider()     
    
    st.subheader("Time Series")

    # Choose numeric columns (excluding the datetime column)
    value_columns = glacierdf.select_dtypes(include=['number']).columns


    # Let user select which column to plot
    selected_column = st.selectbox("Select a value column to plot:", value_columns, index= 3)


    fig = plot_time_series(
        glacierdf,
        x_axis="Topographic Map Year",
        y_axis=selected_column,
        figsize=(10, 5)
    )

    st.pyplot(fig)

    st.divider()

    st.subheader("Time Series Comparison")
    st.write("Select two columns to compare their time series.")
    # Grid layout
    column1, column2 = st.columns(2)

    
    with column1:
        selected_column1 = st.selectbox( "",value_columns, index= 3)

    with column2:
        selected_column2 = st.selectbox("", value_columns, index= 8)
        

    st.write(f"Comparing {selected_column1} and {selected_column2} over time")


    plot = plot_time_series_double(
        glacierdf,
        col1=selected_column1,
        col2=selected_column2,
        x_axis="Topographic Map Year",
        figsize=(10, 5)
    )
    st.pyplot(plot)

    st.divider()

    st.subheader("Correlation Heatmap")
    st.write("This heatmap shows the correlation between different weather variables.")


    heatmap = plot_correlation_heatmap(
        glacierdf.drop(columns=["Glacier ID", "Political Unit", "Continent", "Basin Code", "Location Code", "Glacier Code", "Accumulation Orientation",
"Ablation Orientation"]),
        )

    st.pyplot(heatmap)

    st.divider()


    st.subheader("Advanced Climate EDA")

    colu1 , colu2, colu3 = st.columns(3)

    with colu1:
        plot_type = st.selectbox("Plot Type", ["box", "dist", "scatter", "pairplot"])
        cols = st.multiselect("Columns (for pairplot)", glacierdf.columns, default=[glacierdf.columns[5]]  )
    with colu2:
        x_col = st.selectbox("X-Axis", glacierdf.columns, index = 5)
    with colu3:
        y_col = st.selectbox("Y-Axis", glacierdf.columns, index = 6)

    fig = other_visualize(
        glacierdf,
        plot_type=plot_type,
        x=x_col,
        y=y_col,
        cols=cols,
        title=f"{plot_type.capitalize()} of {y_col} vs {x_col}",
    )

    st.plotly_chart(fig) if 'plotly' in str(type(fig)).lower() else st.pyplot(fig)

    st.divider()