import streamlit as st
from scripts.data_utils import load_data

def show():
    # Data preview
    st.subheader("Data Preview")

    if "glacierdf" not in st.session_state:
        glacierdf = load_data("data/nepal_glacier_data.csv")

        st.session_state.glacierdf = glacierdf

    glacierdf = st.session_state.glacierdf

    st.dataframe(glacierdf, height=200)

    st.divider()
        
    st.markdown("""
    This dataset contains various glacier-related features recorded across different regions of Nepal. The following columns represent key glaciological and geographic data, helping you explore the state and dynamics of glaciers:

    ---

    1. **Glacier Identification** 🆔:  
    - **Glacier ID**: Unique identifier assigned to each glacier.

    ---

    2. **Geographic Location** 🗺️:  
    - **Political Unit**: Administrative region of the glacier.
    - **Continent**: Continent where the glacier is located.
    - **Basin Code**: Hydrological basin identifier.
    - **Location Code**: Regional or sub-basin code.
    - **Glacier Code**: Specific glacier code for classification.
    - **Latitude**: Latitude of the glacier center.
    - **Longitude**: Longitude of the glacier center.

    ---

    3. **Glacier Characteristics** ❄️:  
    - **Primary Class**: Main type of glacier (e.g., debris-covered, clean-ice).
    - **Glacier Source**: Source information of the glacier data.
    - **Glacier Form**: Physical form (e.g., valley, cirque).

    ---

    4. **Elevation and Topography** 🏔️:  
    - **Minimum Elevation**: Lowest elevation point (m).
    - **Minimum Elevation Exposed**: Lowest exposed elevation (m).
    - **Mean Elevation**: Average elevation (m).
    - **Mean Elevation Accumulation**: Mean elevation of accumulation area (m).
    - **Mean Elevation Ablation**: Mean elevation of ablation area (m).
    - **Maximum Elevation**: Highest elevation point (m).
    - **Snow Line Elevation**: Altitude of snow line (m).
    - **Snow Line Accuracy**: Accuracy of snow line measurement.

    ---

    5. **Glacier Size and Shape** 📏:  
    - **Glacier Area**: Total area (km²).
    - **Mean Length**: Average glacier length (km).
    - **Mean Depth**: Estimated average glacier thickness (m).
    - **Height Range**: Elevation difference between maximum and minimum points (m).
    - **Average Slope (deg)**: Average slope angle in degrees.
    - **Compactness**: Ratio indicating glacier compactness.

    ---

    6. **Orientation** 🧭:  
    - **Accumulation Orientation**: Direction of snow accumulation zones.
    - **Ablation Orientation**: Direction of glacier melting zones.

    ---

    7. **Mapping and Observations** 🗂️:  
    - **Topographic Map Year**: Year the glacier was mapped.
    - **Topographic Map Scale**: Scale of the topographic map.
    - **Photograph Year**: Year photographs were taken for the glacier.

    ---

    This glacier dataset provides essential information to perform exploratory data analysis (EDA), feature engineering, and to build predictive models for understanding glacier dynamics and climate impacts in Nepal. 🌍❄️
    """)

    st.divider()
