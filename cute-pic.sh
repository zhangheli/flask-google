K=`curl -s http://www.symmz.com/sitemap_baidu.xml | ack -o 'http://www.symmz.com/\w+/\d+-\d+.html' `
for item in `echo $K`;do
	ack -o 'http://img\S+/\d+max.jpg' html/`cd html && curl -s "$item" -O -w '%{filename_effective}' ` | xargs -L 1 bash -cx  'cd jpg && wget -c $0'
done 
