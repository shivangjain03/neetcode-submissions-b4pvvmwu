class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
            if i=="+":
                a=st.pop()
                b = st.pop()
                res = a+b
                st.append(res)
            if i=="-":
                a=st.pop()
                b = st.pop()
                res = b-a
                st.append(res)
            if i=="*":
                a=st.pop()
                b = st.pop()
                res = a*b
                st.append(res)
            if i=="/":
                a=st.pop()
                b = st.pop()
                res = int(b/a)
                st.append(res)
        return st.pop()

        