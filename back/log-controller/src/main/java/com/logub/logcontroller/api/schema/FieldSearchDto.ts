import
    LogLevel
from_keyword_conflict "~/models/LogLevel"

export enum FieldTypeDto
    Tag,
    FullText,
    Geo,
    Numeric


export interface FieldSearchDto

#    type:
    FieldTypeDto

    name?: string;

#    values:
    string[]

#    negation:
    boolean
