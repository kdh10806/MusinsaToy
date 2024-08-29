package com.toyproject2_5.musinsatoy.member.join.repository;

import com.toyproject2_5.musinsatoy.member.join.dto.MemberDto;
import org.apache.ibatis.annotations.Mapper;

<<<<<<< Updated upstream
import java.lang.reflect.Member;

=======
>>>>>>> Stashed changes
@Mapper
public interface MemberDao {
    void deleteAll();                       // 전체 회원 삭제
    int count();                            // 전체 회원수 카운트
<<<<<<< Updated upstream
    int insertMember(MemberDto memberDto);  // 회원 가입
    MemberDto selectOne(String id);         // 회원 1명 정보 가져오기
=======
    int insertMember(MemberDto memberDto); // 회원 가입
>>>>>>> Stashed changes
}
