import random
import time
import sys
sys.path.append('../')  # noqa
from src.graph import Graph
from src.graph import Queue

start_time = time.time()
# class Queue:
#     def __init__(self):
#         self.storage = []
#         self.size = 0

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if len(self.storage) > 0:
#             return self.storage.pop(0)
#             self.size -= 1

#         else:
#             return None

#     def length(self):
#         return self.size


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] \
                or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # auto increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of
        friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add numUsers users
        for i in range(numUsers):
            self.addUser(f"User {i}")

        # O(n^2)
        # possible_friendships = []
        # for i in range(1, numUsers + 1):
        #     for j in range(1, numUsers + 1):
        #         if i != j and (i, j) not in possible_friendships \
        #                 and (j, i) not in possible_friendships:
        #             possible_friendships.append((i, j))

        # # Create friendships
        # random.shuffle(possible_friendships)
        # total = int((numUsers * avgFriendships) / 2)
        # made_friendship = possible_friendships[:total]

        # for friends in made_friendship:
        #     self.addFriendship(friends[0], friends[1])

        # O(n)
        count = 0
        total = (numUsers * avgFriendships) // 2
        while count < total:
            friendship = (random.randint(1, numUsers),
                          random.randint(1, numUsers))
            if self.addFriendship(friendship[0], friendship[1]):
                count += 1

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # With the Graph class
        # runtime: 1.9708278179168701 seconds 100 users, 20 average
        # runtime: 24.768869876861572 seconds 200 users, 20 average
        # runtime: 24.120848417282104 seconds
        # runtime: 24.88981318473816 seconds
        g = Graph()
        for user in self.users:
            g.add_vertex(user)

        for user in self.friendships:
            for friend in self.friendships[user]:
                g.add_edge(user, friend)

        for friend in self.users:
            path = g.bfs(userID, friend)
            if path is not False:
                visited[friend] = path

        # Without the Graph class but have Queue
        # runtime: 1.8722269535064697 seconds
        # runtime: 27.13098406791687 seconds
        # runtime: 26.577613592147827 seconds
        # runtime: 26.608980178833008 seconds
        # for friend in self.users:
        #     q = Queue()
        #     visit = set()
        #     path = []
        #     q.enqueue([userID])

        #     while len(q.storage) > 0:
        #         node = q.dequeue()
        #         path = node
        #         vnode = node[-1]
        #         if vnode == friend:
        #             visited[friend] = path
        #             pass
        #         visit.add(vnode)
        #         for child in self.friendships[vnode]:
        #             if child not in visit:
        #                 dup_node = node[:]
        #                 dup_node.append(child)
        #                 q.enqueue(dup_node)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

    # Check for the degrees of seperation
    total = 0
    for user in connections:
        length = len(connections[user]) - 1
        if length >= 0:
            total += length
    print(len(connections))
    degrees = total/len(connections)
    print("Degrees:", degrees)
    print("Percentage:", (len(connections)/len(sg.users) * 100))

end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")
