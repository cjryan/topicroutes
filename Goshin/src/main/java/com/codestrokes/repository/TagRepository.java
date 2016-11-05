package com.codestrokes.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.codestrokes.model.Tag;

@RepositoryRestResource(collectionResourceRel = "tags", path="tags")
public interface TagRepository  extends PagingAndSortingRepository<Tag, Long> {

}
