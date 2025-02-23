import inspect
import colorsys
import textwrap
import streamlit as st
import pandas as pd
import pydeck as pdk

colors=[[252.53869454089883, 15.832939279468183, 15.832939279468183], [245.29492879295432, 166.22233345962402, 47.61344045962856], [206.53880386800535, 250.35405167454124, 31.277812641861907], [86.08444374035318, 252.58906414334174, 44.45828863960605], [49.77087522287998, 251.07449995280757, 130.29232511485108], [34.337683403663135, 253.71075041422856, 253.71075041422858], [23.507932628492572, 113.52512290553551, 248.55090832109997], [67.81854547282862, 22.683472932033485, 248.35883563600996], [201.5587841936545, 12.49408890653035, 248.82495801543558], [247.8891328653575, 47.34017156183642, 167.66954834394906]]

ICON_URL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Google_Maps_pin.svg/137px-Google_Maps_pin.svg.png'

icon_data = {
    "url": ICON_URL,
    "width": 137,
    "height": 240,
    "anchorY": 240,
    "mask": True
}

def srcpath(src):
    @st.cache
    def lay(src):
        layers = []
        df=df0.query(f"`src`=={src}")

        for i in range(df.shape[0]):
            layer = pdk.Layer(
                type='PathLayer',
                data=df[i:i+1],
                rounded=True,
                billboard=True,
                pickable=True,
                width_min_pixels=3,
                auto_highlight=True,
                get_color=colors[i],
                get_path='path',
            )
            layers.append(layer)
        
        srclayer = pdk.Layer(
          "ScatterplotLayer",
          data=dfs[src:src+1],
          pickable=True,
          stroked=True,
          filled=True,
          opacity=1,
          get_radius=3999,
          radius_max_pixels=12,
          get_position="coordinates",
          get_fill_color=[0,0,0],
        )
        
        layers.append(srclayer)
        
        iconlayer = pdk.Layer(
            type='IconLayer',
          data=dfs[src:src+1],
            billboard=True,
            get_icon='icon_data',
            get_size=79,
            get_color=[155,155,155],
            size_scale=1,
            size_min_pixels=10,
            opacity=0.6,
            size_max_pixels=100,
            get_position='coordinates',
            pickable=True
        )

        layers.append(iconlayer)

        return layers

    layers = lay(src)

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={"latitude": dfs["coordinates"][src][1], "longitude": dfs["coordinates"][src][0], "zoom": 7, "pitch": 30},
        layers=layers,
    ))

def getpath(src, tp, veh):

    @st.cache
    def lay(src, tp, veh):
        layers = []
        df=df0.query(f"`src`=={src}").query(f"`type`=={tp}").query(f"`veh`=={veh}")

        layer = pdk.Layer(
            type='PathLayer',
            data=df,
            rounded=True,
            billboard=True,
            pickable=True,
            width_min_pixels=3,
            auto_highlight=True,
            get_path='path',
        )
        layers.append(layer)

        srclayer = pdk.Layer(
          "ScatterplotLayer",
          data=dfs[src:src+1],
          pickable=True,
          stroked=True,
          filled=True,
          opacity=1,
          get_radius=3999,
          radius_max_pixels=12,
          get_position="coordinates",
          get_fill_color=[0,0,0],
        )
        
        layers.append(srclayer)
        
        iconlayer = pdk.Layer(
            type='IconLayer',
          data=dfs[src:src+1],
            billboard=True,
            get_icon='icon_data',
            get_size=79,
            get_color=[155,155,155],
            size_scale=1,
            size_min_pixels=10,
            opacity=0.6,
            size_max_pixels=100,
            get_position='coordinates',
            pickable=True
        )

        layers.append(iconlayer)

        return layers

    layers = lay(src, tp,veh)
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={"latitude": dfs["coordinates"][src][1], "longitude": dfs["coordinates"][src][0], "zoom": 8, "pitch": 0},
        layers=layers,
    ))

def fullpath():
    @st.cache
    def lay():
        layers = []

        for i in range(df0['src'].nunique()):
            df=df0.query(f"`src`=={i}")
            layer = pdk.Layer(
                type='PathLayer',
                data=df,
                rounded=True,
                billboard=True,
                pickable=True,
                width_min_pixels=5,
                auto_highlight=True,
                get_color=colors[i],
                get_path='path',
            )
            layers.append(layer)
        return layers

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={"latitude": 48.8566, "longitude": 2.3522, "zoom": 7, "pitch": 0},
        layers=lay(),
    ))

def overview():
    @st.cache
    def lay():
        layers = []

        for i in range(dfd['labels'].nunique()):

            df=dfd.query(f"`labels`=={i}")
         
            layer = pdk.Layer(
              "ScatterplotLayer",
              data=df,
              pickable=True,
              stroked=True,
              filled=True,
              opacity=0.2,
              get_radius=3999,
              radius_max_pixels=19,
              get_position="coordinates",
              get_fill_color=colors[i],
            )
            
            layers.append(layer)

        srclayer = pdk.Layer(
          "ScatterplotLayer",
          data=dfs,
          pickable=True,
          stroked=True,
          filled=True,
          opacity=1,
          get_radius=3999,
          radius_max_pixels=7,
          get_position="coordinates",
          get_fill_color=[0,0,0],
        )
        
        layers.append(srclayer)
        
        iconlayer = pdk.Layer(
            type='IconLayer',
            data=dfs,
            billboard=True,
            get_icon='icon_data',
            get_size=89,
            size_scale=1,
            size_min_pixels=10,
            opacity=0.6,
            size_max_pixels=100,
            get_position='coordinates',
            pickable=True
        )
        layers.append(iconlayer)
        return layers

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={"latitude": 48.8566, "longitude": 2.3522, "zoom": 7, "pitch": 40},
        layers=lay(),
    ))


@st.cache
def getdf():
    df = pd.read_json('srcdf.json')
    df['icon_data'] = None
    for i in df.index:
        df['icon_data'][i] = icon_data
    return [pd.read_json(x) for  x in ['destdf.json','fulldf.json']] + [df]

if __name__ == "__main__":
    dfd, df0, dfs = getdf()

    '''
# NaviX

## AI-based Route Optimization and Visualization Tool for Sales Vehicles

In the fast-developing logistics and supply chain management fields, one of the critical challenges is designing an efficient supply chain that connects multiple destinations and suppliers while optimizing costs. The Multi-Depot Vehicle Routing Problem (MDVRP) addresses this issue by assigning destinations to sources and optimizing vehicle routes under given constraints.

### Clustered Waypoints
```
overview()
```
_(hover and scroll to zoom)_

The interactive map above displays the locations of sources (pins) and destinations (circles) after initial clustering. MDVRP requires assigning destinations to sources and determining the optimal vehicle routes. Each vehicle starts from a source, serves the assigned destinations, and returns to the source while ensuring total demand does not exceed vehicle capacity. The objective is to minimize total travel distance and associated costs.

This project utilizes a heuristic algorithm with the following phases:

* **Phase 1**: Cluster destination nodes to source nodes using a modified K-Means algorithm.
* **Phase 2**: Analyze points to determine vehicle type and count based on constraints.
* **Phase 3**: Assign vehicles to destination subsets using K-Means while minimizing fuel costs.
* **Phase 4**: Optimize routing using _Traveling Salesman Problem_ (TSP) optimization for each vehicle.

Detailed implementation analysis can be found in `prototype.ipynb` within the project repository.

### Routing Demo

'''
    dtype = st.radio("", ('Single vehicle', 'Full demo'), index=0)
    if dtype=='Single vehicle':
        src = st.selectbox(
                'Choose source depot ID',range(10),index=4)
        srcdf0 = df0.loc[df0['src'] == src]
        ntype = srcdf0['type'].nunique()
        tp = st.selectbox(
                'Choose vehicle type',range(int(ntype)+1),index=2,
                format_func=(lambda x: ['Pickup','Truck','Any'][x]))
        if tp != 2:
            vehdf0 = srcdf0.loc[srcdf0['type']==tp]
            veh = st.selectbox(
                    'Choose vehicle ID',range(vehdf0.shape[0]),
                        index=0)
            getpath(src, tp, veh)
        else:
            srcpath(src)
    else:
        st.info('Full demo takes few seconds to load..')
        fullpath()
    st.write("_(hover and scroll to zoom)_")
    '''
### Azure Services Used
* Azure Maps (distance API and routing)
* Azure Machine Learning (training modified K-NN)
* Azure Notebooks (prototyping and data analysis)
* Azure App Service (Web-based deployment using MapBox and Streamlit)
    '''