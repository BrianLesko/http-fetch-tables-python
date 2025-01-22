# Create a table and plot using data fetched from wikipedia

Basic fetch using http request and parse using bs4, Then plot the data using streamlit UI.

[preview.png](preview.png)

## Run locally

``` bash
python3 -m venv myenv
source myenv/bin/activate
pip install streamlit plotly bs4 lxml
python3 fetch.py
streamlit run plot.py
```

Then go to http://localhost:8501 in your browser to see the interactive plot
