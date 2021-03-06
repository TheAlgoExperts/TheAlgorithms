//
//  solution.swift
//  
//
//  Created by ido on 2021/07/07.
//

import Foundation

//단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

func solution(_ s:String) -> String {
    if s.count % 2 == 0 {
        return String("\(Array(s)[s.count/2 - 1])\(Array(s)[s.count/2])")
    } else {
        return String(Array(s)[s.count/2])
    }
}
