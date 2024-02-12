class Node:
    def __init__(self, val= '', prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head
    def visit(self, url: str) -> None:
        curr = Node(url)
        self.curr.next = curr
        curr.prev = self.curr
        self.curr = curr
    def back(self, steps: int) -> str:
        count = steps
        while self.curr.prev and count > 0:
            self.curr = self.curr.prev
            count -= 1
        return self.curr.val
    def forward(self, steps: int) -> str:
        count = steps
        while count > 0 and self.curr.next:
            self.curr = self.curr.next
            count -= 1
        return self.curr.val
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)