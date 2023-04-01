#---------------問題1------------------#
from flask #####(1)#####
#####(2)#####

app = #####(3)#####

@app.route("/")
def index():
    #####問題(4)#####

#--------------------------------------#


#---------------問題3------------------#
@app.route("/calc",methods=['GET','POST'])
def calculation():
    if #####(1)##### == "GET":
        return render_template('calculation.html')
    elif #####(1)##### == "POST":
        top = #####(2)#####['top']
        bottom = #####(2)#####['bottom']
        height = #####(2)#####['height']
        # 台形の計算
        answer = trapezoid_area(top, bottom, height)

        #####(3)#####
        

if __name__ == "__main__":
    app.run(debug=True)

#--------------------------------------#
