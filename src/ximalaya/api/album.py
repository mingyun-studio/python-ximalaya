from typing import TypedDict


class SubscriptInfo(TypedDict):
    albumSubscriptValue: int
    url: str


class AlbumInfo(TypedDict):
    albumId: int
    albumPlayCount: int
    albumTrackCount: int
    albumCoverPath: str
    albumTitle: str
    albumUserNickName: str
    anchorId: int
    anchorGrade: int
    mvpGrade: int
    isDeleted: bool
    isPaid: bool
    isFinished: int
    anchorUrl: str
    albumUrl: str
    intro: str
    vipType: int
    logoType: int
    subscriptInfo: SubscriptInfo
    albumSubscript: int


class AlbumsResponse(TypedDict):
    currentUid: int
    total: int
    pageNum: int
    pageSize: int
    albums: list[AlbumInfo]
