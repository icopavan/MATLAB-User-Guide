ug-nbs = getting_started.ipynb overview.ipynb 00_Scatter_\&_Line_Plots.ipynb

convert: $(ug-nbs)
	ipython nbconvert --to html $(ug-nbs)
	mv $(ug-nbs:ipynb=html) converted/

publish:
	ipython scripts/translate_href-html.py converted/*.html
	ipython scripts/publish.py converted/*.html

link-nbs-to-plotly: $(ug-nbs)
	ipython scripts/translate_href-ipynb.py $(ug-nbs)

push-to-streambed:
	cp -R published/* ../streambed/shelly/api_docs/templates/api_docs/user-guide/matlab

clean-converted:
	rm -f converted/*

clean-published:
	rm -rf published/*

clean: clean-converted clean-published
