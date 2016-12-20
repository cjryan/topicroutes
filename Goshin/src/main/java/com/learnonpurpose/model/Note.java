package com.learnonpurpose.model;

import java.util.Date;
import java.util.List;
import java.util.Set;

import javax.persistence.*;

@Entity
public class Note extends ITemporal {
	
	@Id @GeneratedValue(strategy=GenerationType.IDENTITY)
	Long id;
	
	@Lob
	String note;
	
	@ManyToOne
	Question question;
	
	@ManyToMany(cascade = CascadeType.ALL)
	@JoinTable(name = "note_tag", joinColumns = @JoinColumn(name = "note_id", referencedColumnName = "id"), inverseJoinColumns = @JoinColumn(name = "tag_id", referencedColumnName = "id"))
	Set<Tag> tags;

	public String getNote() {
		return note;
	}

	public void setNote(String note) {
		this.note = note;
	}

	public Question getQuestion() {
		return question;
	}

	public void setQuestion(Question question) {
		this.question = question;
	}

	public Set<Tag> getTags() {
		return tags;
	}

	public void setTags(Set<Tag> tags) {
		this.tags = tags;
	}
}
