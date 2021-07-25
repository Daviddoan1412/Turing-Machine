'''
Author  : Doan Van Chuong BA9-008
Date    : 24/7/2021
Object  : Building a Turing machine that can compute the sum of two binary number and give the result to the output.
'''
class turing_machine_process:
    def __init__(self, process, input_two_binary, state = 0):
        self.transition = {}
        self.state = str(state)
        # Create a series tape have 1000 "_" characters
        self.tape = ''.join(['_']*1000)
        self.top = 1000 // 2 # floor divide
        # Insert input in the middel tape
        self.tape_top = self.tape[:self.top]
        self.tape_bottom = self.tape[self.top:]
        self.tape = self.tape_top + input_two_binary + self.tape_bottom
        # Split each line in process file and assign to correspond with s, a, r, d, s1
        for line in process.splitlines():
            s, a, r, d, s1 = line.split(' ')
            self.transition[s,a] = (r, d, s1)

    def step_turing_machine(self):
        if self.state != 'H':
            a = self.tape[self.top]
            action = self.transition.get((self.state, a))
            if action != None:
                r, d, s1 = action
                self.tape_step_top = self.tape[:self.top]
                self.tape_step_bottom = self.tape[self.top+1:]
                self.tape =  self.tape_step_top + r + self.tape_step_bottom
                if d != '*':
                    if d == 'right':
                        self.top = self.top + 1 
                    else:
                        self.top = self.top - 1
                self.state = s1
                # print(self.tape.replace('_', ''), self.state)

    # Method to run process
    def implement(self, max_step=1000-1):
        i = 0
        while self.state != 'H' and i < max_step: 
            self.step_turing_machine()
            i += 1
        print("This is the result: ",self.tape.replace('_', ''))

def main():
    print("Please enter two binary following the form \"num1_num2\" \n")
    print("Example:1000_1000 \n")
    input_two_binary = input("Enter here: ")
    process = open('prosess.txt').read()
    tm = turing_machine_process(process, input_two_binary)
    tm.implement()

if __name__ == "__main__":
    main()

