package com.learnonpurpose.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.learnonpurpose.model.Question;

@RepositoryRestResource(collectionResourceRel = "questions", path="questions")
public interface QuestionRepository  extends PagingAndSortingRepository<Question, Long> {

}
