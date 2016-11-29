package com.codestrokes.model;

import java.util.Date;
import java.util.List;
import java.util.Set;

import javax.persistence.*;

@Entity
public class Note extends ITemporal {
	
	@Id @GeneratedValue(strategy=GenerationType.IDENTITY)
	Long id;
	
	String note;
	
	@ManyToMany(cascade = CascadeType.ALL)
	@JoinTable(name = "note_tag", joinColumns = @JoinColumn(name = "note_id", referencedColumnName = "id"), inverseJoinColumns = @JoinColumn(name = "tag_id", referencedColumnName = "id"))
	Set<Tag> tags;
}
