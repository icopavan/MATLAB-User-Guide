instructions:
	cat Contributing.md

# List of notebook paths to be used in the plot.ly User Guide
ug-nbs = \
	welcome_home.ipynb \
	getting_started.ipynb \
	overview.ipynb \
	00_Scatter_\&_Line_Plots.ipynb

convert: $(ug-nbs)
	ipython nbconvert --to html $(ug-nbs)
	mv $(ug-nbs:.ipynb=.html) converted/

publish:
	ipython scripts/translate_href-html.py converted/*.html
	ipython scripts/image_map.py converted/*.html
	ipython scripts/publish.py converted/*.html
	ipython scripts/make_config.py
	ipython scripts/make_urls.py
	ipython scripts/make_sitemaps.py

push-to-streambed:
	cp -R published/includes/* ../streambed/shelly/templates/api_docs/includes/user_guide/matlab/
	cp published/matlab_urls.py ../streambed/shelly/api_docs/urls/user_guide/
	cp published/matlab_sitemaps.py ../streambed/shelly/api_docs/sitemaps/user_guide/

link-nbs-to-plotly: $(ug-nbs)
	ipython scripts/translate_href-ipynb.py $(ug-nbs)

clean-converted:
	rm -f converted/*

clean-published:
	rm -rf published/*

clean: clean-converted clean-published
