//
//  MulXCountN.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/13.
//

import Foundation

//함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

func solution(_ x:Int, _ n:Int) -> [Int64] {
    
    let result:[Int64] = Array(1...n).map{Int64($0*x)}
    
    return result
}
