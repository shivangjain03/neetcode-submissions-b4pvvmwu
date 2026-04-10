class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
            else:
                a = st.pop()
                b = st.pop()
                if i =="+":
                    res = a+b
                    st.append(res)
                if i =="-":
                    res = b-a
                    st.append(res)
                if i =="*":
                    res = int(a*b)
                    st.append(res)
                if i =="/":
                    res = int(b/a)
                    st.append(res)
        return st[-1]
                
        