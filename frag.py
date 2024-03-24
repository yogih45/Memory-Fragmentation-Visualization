from matplotlib import pyplot as plt
import math as m

class Tool:
    
    def __init__(self):
        self.memorybuffer=[5,5,5,5,5,5,5,5,5,5]
        self.secmemorybuffer=[]
        self.sizeofblock = 5
        self.buffersize = 5 * 10
        self.no_of_process = 0
        self.algo = None
        self.p = 0
        self.proceslist = []
        self.finallist = []
        self.totalmemory=50

    def userentry(self):
        try:
           self.no_of_process = int(input("Enter the number of processes: "))
        except ValueError:
            print("invalid value")
        for i in range(self.no_of_process):
            try:
              a = int(input(f"Enter the size of process {i+1}: "))
            except ValueError:
                print("invalid value...")
            if a>5:
                print("value reached beyond block limit...")
            else:
                self.proceslist.append(a)


    def fitter(self):
        self.finallist = [x for x in self.proceslist]  

    def visualize(self):
        x = [i for i in range(self.no_of_process)]
        fixeds = [5 for _ in range(self.no_of_process)]
        freespace = [(lambda x, y: x - y)(x, y) for x, y in zip(fixeds, self.finallist)]
        plt.barh(x, self.finallist, color='red', label='Process Sizes(KB)')
        plt.barh(x, freespace, left=self.finallist, label='Free Space(KB)', color='blue')

        plt.ylabel('Processes')
        plt.xlabel('Memory Sizes(KB) ')
        plt.title('Process Sizes')
        plt.legend()
        plt.show()


        
    def show(self):
        print(self.finallist)
    
    def showmemory(self):
        print("Free memory:", self.sizeofblock * 10 - sum(self.finallist),"kb")
    
    def showactmemory(self):
        print("Total Memory:",self.totalmemory,"kb")
    
    def showbuffer(self):
        self.secmemorybuffer = []  
        for i in range(10):
            try:
                n = self.memorybuffer[i] - self.finallist[i]
            except IndexError:
                n = self.memorybuffer[i] - 0
            self.secmemorybuffer.append(n)
        print(self.secmemorybuffer)


    def compaction(self):
        if not self.secmemorybuffer:
            print("No memory buffer available for compaction.")
            return
        
        no_of_blocks = m.floor(sum(self.secmemorybuffer)/5)
        for _ in range(no_of_blocks):
            self.secmemorybuffer.append("new block")
        


    def aftercompacion(self):
        print(self.secmemorybuffer)
    
    def aftervisualizaion(self):
        x = []
        heights = []
        colors = []  # Store colors for each bar
        
        for i, val in enumerate(self.secmemorybuffer):
            if isinstance(val, int):
                x.append(i)
                heights.append(val)
                colors.append('red')  # Numeric values are red
            else:
                x.append(i)
                heights.append(5)  # Setting the height as 5 for non-numeric values
                colors.append('cyan')  # Non-numeric values are cyan
        
        plt.bar(x, heights, color=colors, label='Memory Blocks(KB)')
        plt.ylabel('Blocks')
        plt.xlabel('Memory Sizes(KB)')
        plt.title('Memory Blocks After Compaction')
        plt.show()





tool = Tool() 
tool.showbuffer()
tool.userentry()
tool.fitter()
tool.show()
tool.showactmemory()
tool.showmemory()
tool.visualize()
print("before compacion")
tool.showbuffer()
tool.compaction()
print("after compacion")
tool.aftercompacion()
tool.aftervisualizaion()
