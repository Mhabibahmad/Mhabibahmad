from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor
from lombok import Value

Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Data @AllArgsConstructor @NoArgsConstructor @Builder(toBuilder = true) public class RLogubSchema
class RLogubSchema:

    def __init__(self):
        self.__schema = None
