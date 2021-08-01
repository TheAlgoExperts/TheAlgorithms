//
//  Solution.swift
//  
//
//  Created by ido on 2021/08/01.
//

import Foundation

//자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

func solution(_ n:Int64) -> [Int] {
    
    return String(n).map{ Int(String($0))! }.reversed()
    
}

// 배열을 요소를 역순으로 하는 메소드는 reversed() 기억하자

