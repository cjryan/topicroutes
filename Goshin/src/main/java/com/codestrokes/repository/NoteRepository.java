package com.codestrokes.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.codestrokes.model.Note;

@RepositoryRestResource(collectionResourceRel = "notes", path="notes")
public interface NoteRepository  extends PagingAndSortingRepository<Note, Long> {

}
