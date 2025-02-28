"""
Project 1
CSE 331 SS25
Authors of DLL: Andrew McDonald, Alex Woodring, Andrew Haas, Matt Kight, Lukas Richters, 
                Anna De Biasi, Tanawan Premsri, Hank Murdock, & Sai Ramesh
Authors of Application: Divya Sudha & Leo Specht
solution.py
"""

from __future__ import annotations
from typing import List, TypeVar, Tuple, Optional

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")

# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    DO NOT MODIFY
    """
    __slots__ = ["value", "next", "prev"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        DO NOT MODIFY
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        DO NOT MODIFY
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        :return: True if DLL is empty, else False.
        """
        if self.head is None:
            return True
        return False

    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL;
            if False, add to front (head-end).
        :return: None.
        """
        new_node = Node(val, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if back:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
        self.size += 1
        return

    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        :param back: if True, remove Node from (tail-end) of DLL;
            if False, remove from front (head-end).
        :return: None.
        """
        if self.head is None:
            return
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            elif back:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                self.head.next.prev = None
                self.head = self.head.next
        self.size -= 1
        return

    def list_to_dll(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        self.head = None
        self.tail = None
        self.size = 0
        if not source:  # if list is empty
            return
        self.head = Node(source[0], None, None)
        current_node = self.head
        for i in range(1, len(source)):  # test if works on list of 1 node
            current_node.next = Node(source[i], None, current_node)
            current_node = current_node.next
            if i == len(source) - 1:
                break
        self.tail = Node(source[-1], None, current_node)
        self.size = len(source)
        return

    def dll_to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        :return: standard Python list containing values stored in DLL.
        """
        dll_list = list()
        current_node = self.head
        if self.head is None:
            return dll_list
        while current_node is not None:
            dll_list.append(current_node.value)
            current_node = current_node.next
        return dll_list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Construct list of Nodes with value val in the DLL and return the associated Node list

        :param val: The value to be found
        :param find_first: If True, only return the first occurrence of val. If False, return all
        occurrences of val
        :return: A list of all the Nodes with value val.
        """
        val_list = list()
        current_node = self.head
        if find_first:
            while current_node is not None:
                if current_node.value is val:
                    val_list.append(current_node)
                    break
                current_node = current_node.next
        else:
            while current_node is not None:
                if current_node.value is val:
                    val_list.append(current_node)
                current_node = current_node.next
        return val_list

    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object..

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`.
            If `val` does not exist in DLL, return an empty list.
        """
        found_node = self._find_nodes(val, True)
        if not found_node:
            return None
        else:
            return found_node[0]


    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`.
            If `val` does not exist in DLL, return None.
        """
        found_nodes = self._find_nodes(val)
        return found_nodes

    def _remove_node(self, to_remove: Node) -> None:
        """
        Given a node in the linked list, remove it.

        :param to_remove: node to be removed from the list
        :return: None
        """
        next_node = to_remove.next
        prev_node = to_remove.prev
        if next_node is None and prev_node is None:  # remove sole node
            self.head = None
            self.tail = None
        elif next_node is not None and prev_node is None:  # remove head node
            next_node.prev = None
            self.head = next_node
        elif next_node is None and prev_node is not None:  # remove tail node
            prev_node.next = None
            self.tail = prev_node
        else:  # remove a middle node
            prev_node.next = next_node
            next_node.prev = prev_node
        self.size -= 1
        return

    def remove(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """
        removing_node = self.find(val)
        if removing_node is None:
            return False
        else:
            self._remove_node(removing_node)
            return True

    def remove_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL;
                 if no Node containing `val` exists in DLL, return 0.
        """
        removing_nodes = self.find_all(val)
        removed_count = 0
        for node in removing_nodes:
            size_before = self.size
            self._remove_node(node)
            if self.size is not size_before:
                removed_count += 1
        return removed_count

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the
        DLL and resetting the `head` and `tail` references.

        :return: None.
        """
        if self.size < 2:
            return
        current_node = self.head
        prev_node = None
        while current_node is not None:
            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node
            current_node = current_node.prev
        # reset references
        self.tail = self.head
        self.head = prev_node.prev
        return

class Spotify_Music_Player:
    def __init__(self, paid: bool=False) -> None:
        """
        Initializes the Spotify_Music_Player class

        :param paid: Account type for Spotify
        :return: None
        """
        self.songlist = DLL()
        self.playing = None
        self.paid = paid

    def play_favorite_next(self, favorite_song, forward=True) -> None:
        """
        Changes the song order so that the favorite song is played after the current one

        :param favorite_song: Song to be played next
        :param forward: This tells you where to remove the favorite song node from, in order to move it after the currently playing song, if already in the song list. If True, remove latest node in the tree that contains the favorite song. If False, remove the first occurrence of favorite song and move it to be after the playing node.
        :return: None
        """
        favorite_node = None
        if self.songlist.head is None:  # if empty queue
            self.songlist.head = self.songlist.tail = Node(favorite_song)
            self.songlist.size += 1
            self.playing = self.songlist.head
            return

        if self.songlist.find(favorite_song) is None:  # if not in queue
            favorite_node = Node(favorite_song, self.playing.next, self.playing)
            self.playing.next = favorite_node
            if self.playing.next is not None:
                self.playing.next.prev = favorite_node
            self.songlist.size += 1
            return

        if forward:
            favorite_node = self.songlist.find_all(favorite_song)[-1] # get ready to swap last found instance
        else:
            favorite_node = self.songlist.find(favorite_song)

        if favorite_node is self.songlist.head:  # check favorite node locations
            favorite_node.next.prev = None
            self.songlist.head = favorite_node.next
        elif favorite_node is self.songlist.tail:
            favorite_node.prev.next = None
            self.songlist.tail = favorite_node.prev
        else:
            favorite_node.next.prev = favorite_node.prev
            favorite_node.prev.next = favorite_node.next
        favorite_node.prev = self.playing
        favorite_node.next = self.playing.next
        self.playing.next = favorite_node

        if self.playing is self.songlist.tail:
            self.songlist.tail = favorite_node
            return
        else:
            self.playing.next.prev = favorite_node
        return



    def add_ads(self, advertisement: str, favorite: str) ->None:
        """
        Inserts ads for non-premium Spotify accounts

        :param advertisement: Value of ad to be inserted.
        :param favorite: User's favorite song so ad can be inserted after it.
        """
        if self.paid:
            return
        favorite_nodes = self.songlist.find_all(favorite)
        for fav in favorite_nodes:
            if fav.prev is not None:  # check if not right after fav
                if fav.prev.value is not fav.value:
                    fav.prev.next = fav.prev = Node(advertisement, fav, fav.prev)
            else:
                fav.prev = Node(advertisement, fav, None)
                self.songlist.head = fav.prev
        return



